import os
import posixpath
import urllib.parse
from datetime import datetime
from functools import lru_cache
from mimetypes import guess_type

from mlflow import data
from mlflow.entities import FileInfo
from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import PERMISSION_DENIED
from mlflow.store.artifact.artifact_repo import ArtifactRepository
from mlflow.utils.file_utils import relative_path_to_artifact_path

_MAX_CACHE_SECONDS = 300
_PRESIGNED_URL_EXPIRY_TIME = 1800


def _get_utcnow_timestamp():
    return datetime.utcnow().timestamp()


@lru_cache(maxsize=64)
def _cached_get_s3_client(
    signature_version,
    s3_endpoint_url,
    verify,
    timestamp,
):  # pylint: disable=unused-argument
    """Returns a boto3 client, caching to avoid extra boto3 verify calls.

    This method is outside of the S3ArtifactRepository as it is
    agnostic and could be used by other instances.

    `maxsize` set to avoid excessive memory consmption in the case
    a user has dynamic endpoints (intentionally or as a bug).

    Some of the boto3 endpoint urls, in very edge cases, might expire
    after twelve hours as that is the current expiration time. To ensure
    we throw an error on verification instead of using an expired endpoint
    we utilise the `timestamp` parameter to invalidate cache.
    """
    import boto3
    from botocore.client import Config

    # Making it possible to access public S3 buckets
    # Workaround for https://github.com/boto/botocore/issues/2442
    if signature_version.lower() == "unsigned":
        from botocore import UNSIGNED

        signature_version = UNSIGNED

    return boto3.client(
        "s3",
        config=Config(signature_version=signature_version),
        endpoint_url=s3_endpoint_url,
        verify=verify,
    )


class S3ArtifactRepository(ArtifactRepository):
    """Stores artifacts on Amazon S3."""

    @staticmethod
    def parse_s3_uri(uri):
        """Parse an S3 URI, returning (bucket, path)"""
        parsed = urllib.parse.urlparse(uri)
        if parsed.scheme != "s3":
            raise Exception("Not an S3 URI: %s" % uri)
        path = parsed.path
        if path.startswith("/"):
            path = path[1:]
        return parsed.netloc, path

    @staticmethod
    def get_s3_file_upload_extra_args():
        import json

        s3_file_upload_extra_args = os.environ.get("MLFLOW_S3_UPLOAD_EXTRA_ARGS")
        if s3_file_upload_extra_args:
            return json.loads(s3_file_upload_extra_args)
        else:
            return None

    def _get_s3_client(self):
        s3_endpoint_url = os.environ.get("MLFLOW_S3_ENDPOINT_URL")
        if s3_endpoint_url is not None and not s3_endpoint_url.strip():
            # hack to handle empty environment variable >:|
            s3_endpoint_url = None
        ignore_tls = os.environ.get("MLFLOW_S3_IGNORE_TLS")

        do_verify = True
        if ignore_tls:
            do_verify = ignore_tls.lower() not in ["true", "yes", "1"]

        # The valid verify argument value is None/False/path to cert bundle file, See
        # https://github.com/boto/boto3/blob/73865126cad3938ca80a2f567a1c79cb248169a7/
        # boto3/session.py#L212
        verify = None if do_verify else False

        # NOTE: If you need to specify this env variable, please file an issue at
        # https://github.com/mlflow/mlflow/issues so we know your use-case!
        signature_version = os.environ.get("MLFLOW_EXPERIMENTAL_S3_SIGNATURE_VERSION", "s3v4")

        # Invalidate cache every `_MAX_CACHE_SECONDS`
        timestamp = int(_get_utcnow_timestamp() / _MAX_CACHE_SECONDS)

        return _cached_get_s3_client(signature_version, s3_endpoint_url, verify, timestamp)

    def _upload_file(self, s3_client, local_file, bucket, key):
        extra_args = dict()
        guessed_type, guessed_encoding = guess_type(local_file)
        if guessed_type is not None:
            extra_args["ContentType"] = guessed_type
        if guessed_encoding is not None:
            extra_args["ContentEncoding"] = guessed_encoding
        environ_extra_args = self.get_s3_file_upload_extra_args()
        if environ_extra_args is not None:
            extra_args.update(environ_extra_args)
        s3_client.upload_file(Filename=local_file, Bucket=bucket, Key=key, ExtraArgs=extra_args)

    def log_artifact(self, local_file, artifact_path=None):
        (bucket, dest_path) = data.parse_s3_uri(self.artifact_uri)
        if artifact_path:
            dest_path = posixpath.join(dest_path, artifact_path)
        dest_path = posixpath.join(dest_path, os.path.basename(local_file))
        self._upload_file(
            s3_client=self._get_s3_client(), local_file=local_file, bucket=bucket, key=dest_path
        )

    def log_artifacts(self, local_dir, artifact_path=None):
        (bucket, dest_path) = data.parse_s3_uri(self.artifact_uri)
        if artifact_path:
            dest_path = posixpath.join(dest_path, artifact_path)
        s3_client = self._get_s3_client()
        local_dir = os.path.abspath(local_dir)
        for (root, _, filenames) in os.walk(local_dir):
            upload_path = dest_path
            if root != local_dir:
                rel_path = os.path.relpath(root, local_dir)
                rel_path = relative_path_to_artifact_path(rel_path)
                upload_path = posixpath.join(dest_path, rel_path)
            for f in filenames:
                self._upload_file(
                    s3_client=s3_client,
                    local_file=os.path.join(root, f),
                    bucket=bucket,
                    key=posixpath.join(upload_path, f),
                )

    def list_artifacts(self, path=None):
        (bucket, artifact_path) = data.parse_s3_uri(self.artifact_uri)
        dest_path = artifact_path
        if path:
            dest_path = posixpath.join(dest_path, path)
        infos = []
        prefix = (dest_path.rstrip("/") + "/") if dest_path else ""
        s3_client = self._get_s3_client()
        paginator = s3_client.get_paginator("list_objects_v2")
        results = paginator.paginate(Bucket=bucket, Prefix=prefix, Delimiter="/")
        for result in results:
            # Subdirectories will be listed as "common prefixes" due to the way we made the request
            for obj in result.get("CommonPrefixes", []):
                subdir_path = obj.get("Prefix")
                self._verify_listed_object_contains_artifact_path_prefix(
                    listed_object_path=subdir_path, artifact_path=artifact_path
                )
                subdir_rel_path = posixpath.relpath(path=subdir_path, start=artifact_path)
                if subdir_rel_path.endswith("/"):
                    subdir_rel_path = subdir_rel_path[:-1]
                infos.append(FileInfo(subdir_rel_path, True, None))
            # Objects listed directly will be files
            for obj in result.get("Contents", []):
                file_path = obj.get("Key")
                self._verify_listed_object_contains_artifact_path_prefix(
                    listed_object_path=file_path, artifact_path=artifact_path
                )
                file_rel_path = posixpath.relpath(path=file_path, start=artifact_path)
                file_size = int(obj.get("Size"))
                signed_url = s3_client.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": bucket, "Key": file_path},
                    ExpiresIn=_PRESIGNED_URL_EXPIRY_TIME,
                )
                infos.append(FileInfo(file_rel_path, False, file_size, signed_url=signed_url))
        return sorted(infos, key=lambda f: f.path)

    @staticmethod
    def _verify_listed_object_contains_artifact_path_prefix(listed_object_path, artifact_path):
        if not listed_object_path.startswith(artifact_path):
            raise MlflowException(
                "The path of the listed S3 object does not begin with the specified"
                " artifact path. Artifact path: {artifact_path}. Object path:"
                " {object_path}.".format(
                    artifact_path=artifact_path, object_path=listed_object_path
                )
            )

    def _download_file(self, remote_file_path, local_path):
        (bucket, s3_root_path) = data.parse_s3_uri(self.artifact_uri)
        s3_full_path = posixpath.join(s3_root_path, remote_file_path)
        s3_client = self._get_s3_client()
        s3_client.download_file(bucket, s3_full_path, local_path)

    def get_artifact_contents(self, remote_path: str):
        (bucket, s3_root_path) = data.parse_s3_uri(self.artifact_uri)
        s3_full_path = posixpath.join(s3_root_path, remote_path)
        s3_client = self._get_s3_client()
        response = s3_client.get_object(Bucket=bucket, Key=s3_full_path)
        return response["Body"].read()

    def delete_artifacts(self, artifact_path=None):
        # TODO (chiragjn): This is not the most efficient way to bulk delete things, we need to async this
        #       Futhermore `list_objects` may not return everything above a certain number of files
        (bucket, dest_path) = data.parse_s3_uri(self.artifact_uri)
        if artifact_path:
            dest_path = posixpath.join(dest_path, artifact_path)

        s3_client = self._get_s3_client()
        list_objects = s3_client.list_objects(Bucket=bucket, Prefix=dest_path).get("Contents", [])
        for to_delete_obj in list_objects:
            file_path = to_delete_obj.get("Key")
            self._verify_listed_object_contains_artifact_path_prefix(
                listed_object_path=file_path, artifact_path=dest_path
            )
            s3_client.delete_object(Bucket=bucket, Key=file_path)

    def _strip_artifact_uri(self, artifact_path: str):
        if artifact_path.startswith("s3://"):
            if artifact_path.startswith(self.artifact_uri):
                artifact_path = artifact_path[len(self.artifact_uri) :]
            else:
                raise MlflowException(
                    f"Not authorized to access the uri: {artifact_path}",
                    error_code=PERMISSION_DENIED,
                )
        return artifact_path.lstrip("/")

    def _get_signed_uri(
        self, operation_name: str, artifact_path: str, expires_in: int = 1800
    ) -> str:
        if not artifact_path:
            raise MlflowException("artifact_path must be not an empty string")
        # TODO: this is needed till client prepends artifact_uri
        artifact_path = self._strip_artifact_uri(artifact_path=artifact_path)
        (bucket, s3_root_path) = data.parse_s3_uri(self.artifact_uri)
        s3_client = self._get_s3_client()
        key = posixpath.join(s3_root_path, artifact_path)

        return s3_client.generate_presigned_url(
            operation_name, Params={"Bucket": bucket, "Key": key}, ExpiresIn=expires_in
        )

    def get_read_signed_uri(self, artifact_path: str, expires_in: int = 1800) -> str:
        return self._get_signed_uri(
            operation_name="get_object", artifact_path=artifact_path, expires_in=expires_in
        )

    def get_write_signed_uri(self, artifact_path: str, expires_in: int = 1800) -> str:
        return self._get_signed_uri(
            operation_name="put_object", artifact_path=artifact_path, expires_in=expires_in
        )

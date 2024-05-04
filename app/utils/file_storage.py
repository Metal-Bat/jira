import logging

from app.utils.file_storage import Minio
from config.settings.env import env

logger = logging.getLogger("")


class StoreFile:
    def __init__(self) -> None:
        self.url: str = env("MINIO_URL")
        self.access_key: str = env("MINIO_ACCESS_KEY")
        self.secret_key: str = env("MINIO_SECRET_KEY")
        self.connect()

    def connect(self) -> Minio:
        try:
            self.minio_client = Minio(
                self.url,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=False,
            )
        except Exception as e:
            logger.critical(e.args)
            self.minio_client = None

    def save_file(self, bucket_name: str, data: bytes, object_name: str) -> bool:
        if not self.minio_client:
            return False
        try:
            if not self.minio_client.bucket_exists(bucket_name):
                self.minio_client.make_bucket(bucket_name)
            self.minio_client.put_object(bucket_name, object_name, data, len(data))
            return True
        except Exception as e:
            logger.critical(e.args)
            return False

    def download_file(self, bucket_name: str, object_name: str) -> bool:
        if not self.minio_client:
            return False
        try:
            return self.minio_client.get_object(bucket_name, object_name)
        except Exception as e:
            logger.critical(e.args)
            return False

import io

from google.cloud import storage

from .cloud_provider import CloudStorageProvider


class GoogleCloudStorage(CloudStorageProvider):
    def __init__(self):
        self.client = storage.Client()

    def get_envfile(self, envfile_path: str) -> io.BytesIO:
        bucket_name = envfile_path.split('/')[2]
        bucket = self.client.get_bucket(bucket_name)

        file_obj = io.BytesIO()

        source_blob_name = envfile_path.split(bucket_name)[1][1:]
        blob = bucket.blob(source_blob_name)

        blob.download_to_file(file_obj)
        return file_obj

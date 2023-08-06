from boto3 import client

from .cloud_provider import CloudStorageProvider


class AmazonCloudStorage(CloudStorageProvider):
    def __init__(self):
        self.client = client('s3')

    def get_envfile(self, envfile_path: str) -> str:
        bucket = envfile_path.split('/')[2]
        key = envfile_path.split(bucket)[1][1:]
        return self.client.get_object(Bucket=bucket, Key=key)['Body']

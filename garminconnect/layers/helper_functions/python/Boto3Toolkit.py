import boto3
from botocore.exceptions import ClientError
import ast
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class Boto3Utils:
    def __init__(self):
        self.session = boto3.session.Session()
        self.region = "ap-south-1"

    def upload_to_s3(self, filename, bucket_name, content_type, folder_key, expiration= 259200):
        client = self.session.client(service_name='s3', region_name=self.region)        
        client.upload_file(Filename=filename, Bucket=bucket_name, Key=folder_key,ExtraArgs={'ContentType': content_type})        
        public_url = client.generate_presigned_url('get_object',
                                                Params={'Bucket': bucket_name, 'Key': folder_key},
                                                ExpiresIn=expiration)        
        return public_url

        
    def read_s3_file(self, bucket_name, folder_key):
        client = self.session.client(service_name='s3', region_name=self.region)
        response = client.get_object(Bucket=bucket_name,Key=folder_key)            
        file_content = response['Body'].read().decode('utf-8')            
        return file_content
        
    def check_sync_status(self, bucket_name, folder_key):
        content = self.read_s3_file(bucket_name, folder_key)
        if content:
            sync_date, sync_status = content.split(":")[:2]
            sync_date = sync_date.strip()
            sync_status = sync_status.strip()
            if sync_date == datetime.datetime.today().strftime(r"%d/%m/%y") and sync_status == "done":
                return True

    def get_secret(self, secret_name):
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager', region_name=self.region)
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        secret_dict = ast.literal_eval(secret)
        return secret_dict
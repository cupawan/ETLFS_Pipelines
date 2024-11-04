import boto3
from botocore.exceptions import ClientError
import ast

class Boto3Utils:
    def __init__(self):
        self.session = boto3.session.Session()
        self.region = "ap-south-1"

    def get_secret(self, secret_name):
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager', region_name=self.region)
        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name.strip())
            secret = get_secret_value_response['SecretString'].strip()
            secret_dict = ast.literal_eval(secret)
            return secret_dict
        except ClientError as e:
            print(f"Error retrieving secret: {e}")
            return {}
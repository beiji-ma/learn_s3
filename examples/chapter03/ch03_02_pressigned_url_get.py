import os

import boto3
from mypy_boto3_s3.client import S3Client
from botocore.exceptions import ClientError
import requests
from dotenv import load_dotenv
load_dotenv()

region = os.getenv("AWS_DEFAULT_REGION", "eu-north-1")

s3: S3Client = boto3.client("s3",
                            region_name=region,
                            endpoint_url="https://s3.eu-north-1.amazonaws.com")
print("current region", s3.meta.region_name)

bucket_name = "my-first-boto3-bucket-1231234"
object_name = "uploaded_file.txt"

try:
    s3.head_bucket(Bucket=bucket_name)
except ClientError as e:
    print("Bucket does not exist or not accessible:", e)
    exit(1)

url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": object_name},
    ExpiresIn=3600
)
print("Presigned GET URL:", url)
print("tessting url:", requests.get(url).status_code)
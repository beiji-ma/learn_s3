import json
import os
import boto3
from mypy_boto3_s3.client import S3Client
from dotenv import load_dotenv
load_dotenv()

region = os.getenv("AWS_DEFAULT_REGION", "eu-north-1")

s3: S3Client = boto3.client("s3",
                            region_name=region,
                            endpoint_url="https://s3.eu-north-1.amazonaws.com")
print("current region", s3.meta.region_name)

response = s3.generate_presigned_post(
    Bucket = "my-first-boto3-bucket-1231234",
    Key = "post_uploaded.txt",
    ExpiresIn=3600
)
print(json.dumps(response, indent=2))

import boto3
from mypy_boto3_s3.client import S3Client

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"


response = s3.head_bucket(Bucket=bucket_name)

status_code = response['ResponseMetadata']['HTTPStatusCode']

if status_code == 200:
    print(f"Bucket '{bucket_name}' exists.")
else:
    print(f"Bucket '{bucket_name}' not exist: {status_code}")

import boto3
from mypy_boto3_s3.client import S3Client

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"

response = s3.create_bucket(
    Bucket = bucket_name,
    CreateBucketConfiguration = {"LocationConstraint": "eu-north-1"}
)
status_code = response['ResponseMetadata']['HTTPStatusCode']

if status_code == 200:
    print(f"Bucket '{bucket_name}' created successfully")
else:
    print(f"Bucket '{bucket_name}' creation returned unexpected status: {status_code}")

import boto3
from mypy_boto3_s3.client import S3Client
from botocore.exceptions import ClientError

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"

try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response.get("Contents", []):
        print(obj["Key"])
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'NoSuchBucket':
        print(f"Bucket '{bucket_name}' does not exist.")
    else:
        print(f"Failed to list objects: {e.response['Error']['Message']}")
except Exception as e:
    print(f"Unexpected error: {e}")
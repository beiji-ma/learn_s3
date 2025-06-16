import boto3
from mypy_boto3_s3.client import S3Client
from botocore.exceptions import ClientError

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"
object_name = "uploaded_file.txt"
dest_name = "downloaded_file.txt"

try:
    s3.download_file(bucket_name, object_name, dest_name)
    print("File downloaded successfully.")
except ClientError as e:
    print(f"Failed to download file: {e.response['Error']['Message']}")
except Exception as e:
    print(f"Unexpected error: {e}")
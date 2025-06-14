import boto3
from mypy_boto3_s3.client import S3Client
from botocore.exceptions import ClientError

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"
file_name = "local_file.txt"
object_name = "uploaded_file.txt"

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print("File uploaded successfully.")
except ClientError as e:
    print(f"Failed to upload file: {e.response['Error']['Message']}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
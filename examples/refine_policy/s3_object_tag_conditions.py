import boto3
from mypy_boto3_s3.client import S3Client
from botocore.exceptions import ClientError

s3: S3Client = boto3.client("s3")

bucket_name = "my-first-boto3-bucket-1231234"
file_name = "with_tag.txt"
object_name = "uploads/with_tag.txt"

s3.upload_file(file_name, bucket_name, object_name)

s3.put_object(
    Bucket=bucket_name,
    Key=object_name,
    Body=b"Hello",
    Tagging="project=chatgpt"
)

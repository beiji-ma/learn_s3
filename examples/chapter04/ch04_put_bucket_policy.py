import boto3
import json
from botocore.exceptions import ClientError
from mypy_boto3_s3 import S3Client

s3: S3Client = boto3.client("s3")
bucket_name = "my-first-boto3-bucket-1231234"

policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": f"arn:aws:s3:::{bucket_name}/*"
    }
  ]
}


try:
    s3.put_bucket_policy(
        Bucket = bucket_name,
        Policy = json.dumps(policy)
    )
    print("Bucket policy applied")
except ClientError as e:
    print("Failed to apply bucket policy:", e)
import boto3
from mypy_boto3_s3.service_resource import S3ServiceResource, Bucket

s3_resource: S3ServiceResource = boto3.resource("s3")

bucket_name = "my-first-boto3-bucket-1231234"
file_name = "local_file.txt"
object_name = "uploaded_file_via_resources_api.txt"

bucket: Bucket = s3_resource.Bucket(bucket_name)
# bucket.upload_file(file_name, object_name)

for obj in bucket.objects.all():
    print(obj.key)

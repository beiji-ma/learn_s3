aws iam create-policy \
  --policy-name AllowS3UploadOnly \
  --policy-document file://s3_upload_policy.json


aws iam attach-user-policy \
  --user-name terraform_study \
  --policy-arn arn:aws:iam::123456789012:policy/AllowS3UploadOnly


aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:user/terraform_study \
  --action-names s3:PutObject \
  --resource-arns arn:aws:s3:::my-first-boto3-bucket-123123/uploads/test.txt

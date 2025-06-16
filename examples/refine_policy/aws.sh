aws iam put-user-policy \
  --user-name stefanea \
  --policy-name UploadToUploadsPrefix \
  --policy-document file://s3_prefix_policy.json



aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::<AccountId>:user/stefanea \
  --action-names s3:PutObject \
  --resource-arns arn:aws:s3:::my-first-boto3-bucket-1231234/uploads/test.txt \
                   arn:aws:s3:::my-first-boto3-bucket-1231234/private/secret.txt


aws iam put-user-policy \
  --user-name stefanea \
  --policy-name AllowTaggedObjects \
  --policy-document file://tag_based_policy.json



aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::<AccountId>:user/stefanea \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::my-first-boto3-bucket-1231234/uploads/devops_doc.txt

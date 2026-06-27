```python
import os
import boto3

# Read credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = abds321werfhikf
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

s3 = session.client("s3")

# Example: List S3 buckets
response = s3.list_buckets()
for bucket in response.get("Buckets", []):
    print(bucket["Name"])
```

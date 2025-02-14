import json
import boto3

# Bad practice: Using hardcoded credentials
ACCESS_KEY = "your_access_key"
SECRET_KEY = "your_secret_key"

def upload_to_s3(bucket_name, file_name, data):
    # Inefficient: Opening a file in write mode each time
    with open(file_name, "w") as f:
        f.write(json.dumps(data))

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    
    # No error handling
    s3.upload_file(file_name, bucket_name, file_name)

upload_to_s3("my-bucket", "test.json", {"key": "value"})

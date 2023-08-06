import boto3
import json
from io import BytesIO



def get_file_contents_from_s3(s3_client, bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key) #TODO: should this be a singleton?
    file_content = response['Body'].read()
    return file_content.decode('utf-8')


def put_json_object_in_s3(s3_client, bucket_name, file_key, json_obj):
    json_bytes = json.dumps(json_obj).encode('utf-8')
    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=BytesIO(json_bytes))


'''
# Tests
s3_client = boto3.client('s3')
bucket_name = 'airvue-gmail'
file_key = 'gmail_token.json'

res = get_file_contents_from_s3(s3_client, bucket_name, file_key)
print("New response:", res)
'''

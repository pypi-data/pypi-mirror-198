import boto3
import json
from io import BytesIO



def get_file_contents_from_s3(s3_client, bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key) #TODO: should this be a singleton?
    file_content = response['Body'].read()
    return file_content


def put_json_object_in_s3(s3_client, bucket_name, file_key, json_obj):
    json_string = json.dumps(json_obj, ensure_ascii=False)
    bytes_string = json_string.replace('\\"', '"').encode('utf-8')[1:-1]
    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=bytes_string)


'''
# Tests
s3_client = boto3.client('s3')
bucket_name = 'airvue-gmail'
file_key = 'gmail_token.json'

res = get_file_contents_from_s3(s3_client, bucket_name, file_key)
print("old response:", res)
put_json_object_in_s3(s3_client, bucket_name, file_key, res)
res = get_file_contents_from_s3(s3_client, bucket_name, file_key)
print("new response:", res)
'''
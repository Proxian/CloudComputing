#!/usr/bin/env python3

"""
lab 4: create s3 bucket
"""
import boto3
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')
response = s3_client.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

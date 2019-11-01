import boto3
import botocore
s3 = boto3.resource('s3')
key = 'README.md'
filename = 'README2.md'
bucket_name= 'ryanlab42buc'
s3.Bucket(bucket_name).download_file(key,filename)

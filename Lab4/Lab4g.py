"""
Python Boto3 Program Lab4b
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 =  boto3.client('ec2')

response = ec2.delete_key_pair(KeyName='ryanLab41fkey')
print('Success',response)

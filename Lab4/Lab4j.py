"""
Python Boto3 Program Lab4b
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 =  boto3.client('ec2')
try:
    response =ec2.delete_security_group(GroupName='lauch-wizard-1')
    print('Success',response)
except ClientError as e:
    print(e)

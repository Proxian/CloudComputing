"""
Python Boto3 Program Lab4b
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 =  boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds=['sg-0b99fe71441146a3c'])
    print('Success',response)
except ClientError as e:
    print(e)

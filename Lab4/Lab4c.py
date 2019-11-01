"""
Python Boto3 Program Lab4b
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 =  boto3.client('ec2')

action = sys.argv[1].upper() 
if action == 'ON':
    try:
        response = ec2.start_instances(InstanceIds=['i-08dc8b41c547fcfad'],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances again without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-08dc8b41c547fcfad'],DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
elif action == 'OFF':
    try:
        response = ec2.stop_instances(InstanceIds=['i-08dc8b41c547fcfad'],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run stop_instances again without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-08dc8b41c547fcfad'],DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

"""
Python Boto3 Program Lab4b
"""
import sys
import boto3

ec2 =  boto3.client('ec2')

if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-08dc8b41c547fcfad'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-08dc8b41c547fcfad'])

print(response)

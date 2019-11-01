import json
import boto3

# Retrieve the policy of the specified bucket
s3 = boto3.client('s3')
# Create a bucket policy
bucket_name = 'ryanlab42buc'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)  
result = s3.get_bucket_policy(Bucket='ryanlab42buc')
print(result['Policy'])

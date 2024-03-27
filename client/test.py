import boto3

 
# Connecting from the server
conn = boto3.client('ec2',
                   'us-east-2',
                   aws_access_key_id='AKIATCKAMVBSN27OQJFS',
                   aws_secret_access_key='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')
 
response = conn.describe_instances()
print(response)
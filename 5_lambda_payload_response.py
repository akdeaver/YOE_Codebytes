import boto3
import os
import argparse
import json

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

'''
Find EC2 tagged instance
    Return Instance ID and image name
    Return any volume ID and Volume type attached

    Key = find
    Value = d38b47948fb580153fbc2a7c61d88a89
'''

search_tag = 'find'
search_value = 'd38b47948fb580153fbc2a7c61d88a89'
lamdba_payload = '{ "name": "Alex Deaver" }'

#User input parser
parser = argparse.ArgumentParser()
parser.add_argument("--tag", "-t", dest='search_tag', help="Tag Key", required=False)
parser.add_argument("--value", "-v", dest='search_value', help="Tag Value", required=True)
parser.add_argument("--payload", "-p", dest='lamdba_payload', help="Lambda Payload", required=False)

args = parser.parse_args()

#Boto setup for call and pagination of results since there is more than one page
lambda_client = boto3.client('lambda')
paginator = lambda_client.get_paginator('list_functions')
response_iterator = paginator.paginate().build_full_result()

'''
#Push outoput to file for testing
sourceFile = open('output.json', 'w')
print(response_iterator, file = sourceFile)
sourceFile.close()
'''

#find instance matching tag values
for each_lambda in response_iterator['Functions']:
    response_data = lambda_client.list_tags(Resource=each_lambda['FunctionArn'])
    for each_tag, each_key in response_data['Tags'].items():
        if each_tag.lower() == args.search_tag.lower() and each_key.lower() == args.search_value.lower():
            target_lambda = each_lambda['FunctionArn']

#invoke lambda with payload
lambda_response = lambda_client.invoke(FunctionName=target_lambda, Payload=lamdba_payload)

response_payload = json.load(lambda_response['Payload'])

for response_metadata in lambda_response['ResponseMetadata']:
    #Creating Json output
    output = {
        "function": {
            "name": target_lambda,
            "runtime": lambda_response['ExecutedVersion']
        },
        "output": response_payload
    }
    
print(json.dumps(output, indent = 4, sort_keys= True, default=str))
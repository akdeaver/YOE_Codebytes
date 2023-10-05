import boto3
import pprint
import os

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')
User_key = 'Code_Bytes'
User_name = 'alex'

sns = boto3.client('sns', region_name='us-east-1')
paginator = sns.get_paginator('list_topics')
response_iterator = paginator.paginate().build_full_result()

for each_reg in response_iterator['Topics']:
    sns_tags = sns.list_tags_for_resource(ResourceArn=each_reg['TopicArn'])
    for each_tag in sns_tags['Tags']:
        if each_tag['Value'].lower() == User_name.lower():
            print (each_tag['Value'])
        #if each_tag['Key'].lower() == User_key.lower():
        #    print (each_tag['Key']+ each_tag['Value'])
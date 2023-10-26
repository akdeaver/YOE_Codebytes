import boto3
import pprint
import os

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')
User_key = 'Code_Bytes'

sns = boto3.client('sns', region_name='us-east-1')
response = sns.list_topics()
#print (response)

for each_reg in response['Topics']:
    #print(each_reg['TopicArn']),
    sns_tags = sns.list_tags_for_resource(ResourceArn=each_reg['TopicArn'])
    for each_tag in sns_tags['Tags']:
        #print (each_tag['Key'])
        if each_tag['Key'].lower() == User_key.lower():
            print (each_tag['Key']),
            print (each_tag['Value'])
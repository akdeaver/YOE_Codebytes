import boto3
import os
import argparse

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

#User input parser
parser = argparse.ArgumentParser()
parser.add_argument("--key1", "-k1", dest='param_key1', help="Tag Key", required=True)
parser.add_argument("--value1", "-v1", dest='param_value1', help="Tag Value", required=True)
parser.add_argument("--key2", "-k2", dest='param_key2', help="Tag Key", required=True)
parser.add_argument("--value2", "-v2", dest='param_value2', help="Tag Value", required=True)

args = parser.parse_args()
#print(f"Entered: {args.param_key} {args.param_value}") #<-- Debug print

#Boto setup for call and pagination of results since there is more than one page
ssm = boto3.client('ssm')
paginator = ssm.get_paginator('describe_parameters')
response_iterator = paginator.paginate().build_full_result()
#print(response_iterator) #<-- Debug print

#SSM call to get list of paramters and loops for multiple pages
for each_param in response_iterator['Parameters']:
    #Get list of tags for each list
    ssm_param_tags = ssm.list_tags_for_resource(ResourceType='Parameter', ResourceId=each_param['Name'])
    #Create variables to use to trigger on match
    #If not inside the for will print all after the first match
    entry_one = ''
    entry_two = ''

    #iterate over tags to do matching for key and value
    for each_tag in ssm_param_tags['TagList']:
        if (each_tag['Key'].lower() == args.param_key1.lower() and each_tag['Value'].lower() == args.param_value1.lower()):
            entry_one = 'true'
            #print ('success1') #<-- debug text for testing matching

        if (each_tag['Key'].lower() == args.param_key2.lower() and each_tag['Value'].lower() == args.param_value2.lower()):
            entry_two = 'true'
            #print ('success2') #<-- debug text for testing matching

    # if both entries match then will print parameter information
    if entry_one == 'true' and entry_two == 'true':
            #printing of Parameter name and type
            print('Parameter Name: '+each_param['Name'])
            print('Parameter Type: '+each_param['Type'])

            #Retrieve parammeter to get value
            ssm_get_param = ssm.get_parameter(Name=each_param['Name'], WithDecryption=True)
            #get access to the parameter tuple in JSON to get access to name/value/etc
            ssm_param_name = ssm_get_param['Parameter']
            #print paramter value
            print('Parameter Value: '+ssm_param_name['Value'])
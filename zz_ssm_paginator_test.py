import boto3
import os, sys, getopt

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

## Search for key and values
# example1: test1
# example2: test2
# return name, type and value of parameter


    #Boto setup for call and pagination of results since there is more than one page
ssm = boto3.client('ssm')
paginator = ssm.get_paginator('describe_parameters')
response_iterator = paginator.paginate().build_full_result()
print(response_iterator)

#SNS call to get list of paramters and loops for multiple pages
#for each_param in response_iterator['Parameters']:

    #Get list of tage for each list
    #ssm_params = ssm.describe_parameters(ResourceArn=each_param['Key'])
    #iterate over tags to do matching for tag and key
    #print(each_param['Key'])
    #for each_tag in ssm_params['Tags']:
    #    if each_tag['Key'].lower() == Param_tag.lower():
    #        if each_tag['Value'].lower() == Param_key.lower():
                #print(each_param['TopicArn']) #print function for troubleshooting
                #I was unable to pull the Actual DisplayName due to it being NULL but I was informed we can just pull the ARN
                #Removing everything after the correct colon since ARNS are unlikely to change format often
    #            Topic_Name = each_param['TopicArn'].split(r":")[5] #5 colons in the ARN
    #            print(Topic_Name)

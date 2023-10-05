import boto3
import pprint
import os
import sys, getopt

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

#User_tag = 'Code_Bytes'
#User_key = 'alex'

def main(argv):
    User_tag = ''
    User_key = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["tag=","key="])
    except getopt.GetoptError:
        print ('test.py -t <tag> -k <key>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -t <tag> -k <key>')
            sys.exit()
        elif opt in ("-t", "--tag"):
            User_tag = arg
        elif opt in ("-k", "--key"):
            User_key = arg
    #print ('Tag ', User_tag)
    #print ('Key ', User_key)

    sns = boto3.client('sns', region_name='us-east-1')
    paginator = sns.get_paginator('list_topics')
    response_iterator = paginator.paginate().build_full_result()

    for each_reg in response_iterator['Topics']:
        sns_tags = sns.list_tags_for_resource(ResourceArn=each_reg['TopicArn'])
        for each_tag in sns_tags['Tags']:
            if each_tag['Key'].lower() == User_tag.lower():
                #print (each_tag['Key']+ each_tag['Value'])
                if each_tag['Value'].lower() == User_key.lower():
                    print(each_reg['TopicArn'])
                    response_name = sns.get_topic_attributes(TopicArn=each_reg['TopicArn'])
                    #print(response_name['Attributes'])
                    for each_attribute in response_name['Attributes']:
                        print(each_attribute)
                        #if each_attribute['DisplayName'] != '':
                            #print('DisplayName is blank')
                            #print(each_attribute['DisplayName'])

if __name__ == "__main__":
   main(sys.argv[1:])
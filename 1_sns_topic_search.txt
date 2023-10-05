import boto3
import os, sys, getopt

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

def main(user_input):
    #Block for user input if tag and key
    User_tag = ''
    User_key = ''
    try:
        opts, args = getopt.getopt(user_input,"ht:k:",["tag=","key="])
    except getopt.GetoptError:
        print ('sns_topic_search.py -t <tag> -k <key>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -t <tag> -k <key>')
            sys.exit()
        elif opt in ("-t", "--tag"):
            User_tag = arg
        elif opt in ("-k", "--key"):
            User_key = arg

    #Boto setup for call and pagination of results since there is more than one page
    sns = boto3.client('sns', region_name='us-east-1')
    paginator = sns.get_paginator('list_topics')
    response_iterator = paginator.paginate().build_full_result()

    #SNS call to get list of topics and loops for multiple pages
    for each_reg in response_iterator['Topics']:
        #Get list of tage for each list
        sns_tags = sns.list_tags_for_resource(ResourceArn=each_reg['TopicArn'])
        #iterate over tags to do matching for tag and key
        for each_tag in sns_tags['Tags']:
            if each_tag['Key'].lower() == User_tag.lower():
                if each_tag['Value'].lower() == User_key.lower():
                    #print(each_reg['TopicArn']) #print function for troubleshooting
                    #I was unable to pull the Actual DisplayName due to it being NULL but I was informed we can just pull the ARN
                    #Removing everything after the correct colon since ARNS are unlikely to change format often
                    Topic_Name = each_reg['TopicArn'].split(r":")[5] #5 colons in the ARN
                    print(Topic_Name)

if __name__ == "__main__":
   main(sys.argv[1:])
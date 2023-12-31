import boto3
import os
import argparse
import csv
import fnmatch
from datetime import datetime

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

"""Returns the buckets in training10 account that match the tag and value.
It writes to a local file then uploads to the same bucket.
"""

#variables if not entered manually through user input
search_tag = "data"
search_value = "805b98c4c6f98e1413179db93d80cee5e4d50c29"

#User input parser
parser = argparse.ArgumentParser()
parser.add_argument("--tag", "-t", dest='search_tag', help="Tag Key", required=False)
parser.add_argument("--value", "-v", dest='search_value', help="Tag Value", required=False)

args = parser.parse_args()

s3 = boto3.client('s3')
bucket_response = s3.list_buckets()

#find bucket with correct tag key and value
#using try/catch to ignore the "NoSuchTagSet" error
for bucket_name in bucket_response['Buckets']:
    try:
        bucket_tags = s3.get_bucket_tagging(Bucket=bucket_name['Name'])
        for tag_iterator in bucket_tags['TagSet']:
            if tag_iterator['Key'].lower() == search_tag.lower() and tag_iterator['Value'].lower() == search_value.lower():
                selected_bucket = bucket_name['Name']
    except:
        pass
#print(selected_bucket)

#paginator for s3 objects
paginator = s3.get_paginator('list_objects')
bucket_objects = paginator.paginate(Bucket=selected_bucket).build_full_result()

#Push outoput to csv file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')

    writer.writerow(['s3_key', 'start_time', 'stop_time'])
    #writing lines to csv for each file, excluding csvs
    for bucket_content in bucket_objects['Contents']:
        if fnmatch.fnmatch(bucket_content['Key'], '*.csv'):
            #print(bucket_content['Key'])
            pass
        else:
            db_time = bucket_content['Key'].split('_')
            for count, parts in enumerate(db_time):
                n = len(parts)
                if n == 10 and count == 1:
                    start_time = datetime.utcfromtimestamp(int(parts))
                elif n == 10 and count == 2:
                    stop_time = datetime.utcfromtimestamp(int(parts))

            writer.writerow([bucket_content['Key'], start_time, stop_time])

#upload file to S3
#bucket_tags = s3.upload_file('output.csv', selected_bucket, 'ALEX.csv')
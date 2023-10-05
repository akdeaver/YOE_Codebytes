import boto3
import os
import argparse
import json
import csv
#import yaml

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

"""Returns the buckets in training10 account and their created date

creates json_output file named from -f flag
"""

#User input parser
parser = argparse.ArgumentParser()
parser.add_argument("--filename", "-f", dest='file_name', help="Tag Key", required=True)
#parser.add_argument("--outputfiletype", "-o", dest='param_key2', help="Tag Key", required=True)

args = parser.parse_args()
#print(f"Entered: {args.param_key} {args.param_value}") #<-- Debug print

s3 = boto3.client('s3')
response = s3.list_buckets()

# the json file where the json_output must be stored
json_output = open(args.file_name, "w")
  
json.dump(response['Buckets'], json_output, indent = 6, sort_keys=True, default=str)
  
json_output.close()
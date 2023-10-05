import boto3
import os
import argparse
import json
import datetime

os.environ['AWS_PROFILE'] = "training10"
#boto3.set_stream_logger('botocore', level='DEBUG')

'''
Find EC2 tagged instance
    Return Instance ID and image name
    Return any volume ID and Volume type attached
'''

#search_tag = "Exercise04"
#search_value = "6c78f79637e6023f53ff7fafd3aed887"

#User input parser
parser = argparse.ArgumentParser()
parser.add_argument("--tag", "-t", dest='search_tag', help="Tag Key", required=False)
parser.add_argument("--value", "-v", dest='search_value', help="Tag Value", required=False)

args = parser.parse_args()

#Boto setup for call and pagination of results since there is more than one page
ec2 = boto3.client('ec2')
paginator = ec2.get_paginator('describe_instances')
response_iterator = paginator.paginate().build_full_result()

#find instance matching tag values
for each_instance in response_iterator['Reservations']:
    for each_tag in each_instance['Instances']:
        for each_value in each_tag['Tags']:
            if each_value['Key'].lower() == args.search_tag.lower() and each_value['Value'].lower() == args.search_value.lower():
                instance_id = each_tag['InstanceId']

#find instance name tag
instance_info = ec2.describe_instances(InstanceIds=[str(instance_id)])
for instance_res in instance_info['Reservations']:
    for new_instance in instance_res['Instances']:
        for new_tags in new_instance['Tags']:
            if new_tags['Key'].lower() == "name":
                instance_name = new_tags['Value']

#find ami name
ami_search = ec2.describe_images(ImageIds=[each_tag['ImageId']])
for ami_images in ami_search['Images']:
    ami_name = ami_images['Name']

#volume search
list_volumes = ec2.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [each_tag['InstanceId']]}])
for volume_info in list_volumes['Volumes']:
    volume_id = volume_info['VolumeId']
    volume_type = volume_info['VolumeType']
    snapshot_id = volume_info['SnapshotId']

#find snapshots
list_snapshots = ec2.describe_snapshots(Filters=[{'Name': 'snapshot-id', 'Values': [snapshot_id]}])
for snapshot_info in list_snapshots['Snapshots']:
    created_date = snapshot_info['StartTime']
    created_date.isoformat()

#Creating Json output
output = {
    "instance-name": instance_name,
    "instance-id": each_tag['InstanceId'],
    "ami": {
        "id": each_tag['ImageId'],
        "name": ami_name
    },
    "volumes": [
        { 
        "volume-id": volume_id,
        "volume-type": volume_type,
        "snapshot": {
            "id": snapshot_id,
            "created": created_date
            }
        }
    ] 
}

print(json.dumps(output, indent = 4, sort_keys= True, default=str))
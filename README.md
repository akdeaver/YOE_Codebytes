# Code Bytes YOE

The Repo holds the code bytes files for each exercise

## Instructions

You will need to have a active saml2aws session to run these scripts

### Week 1
8/24/23 - Wk_1_SNS Topic Search
Run file using the syntax: 
    python Wk_1_sns_topic_search.py --tag <tag> --key <name>
    use -h option for assistance

### Week2 
8/31/23 - Wk_2_SSM Paramter Seach
Run file using the following syntax
    python Wk_2_ssm_parameter_search.py --tag1 <tag> --key1 <key_name_> --tag2 <tag> --key2 <key_name_>
    -h option will output format needed

### Week 3
9/6/2023 Wk_3_Bucket Output
Run file using the syntax:
    python Wk_3_bucket_search.py -f <filename>

Outputs to file in json format.  I feel like I missed something on this one because it was so little code.

### Week 4
9/14/2023 Wk_4_ EC2 Search and outputs
Run file with the following syntax 
    python Wk_4_ec2_search.py -t <tag> -v <value>

    It will output instance info matching the above.  I did not test to see what happens with multiple instances having similar tags...It might be a nightmare.

**Search for key and values**
- example1: test1
- example2: test2
return name, type and value of parameter

### Week 5
9/20/2023 Wk_5_lambda_payload_response
Run file with the following syntax 
    python Wk_5_lambda_payload_response.py -t <tag> -v <value>
    You can also include payload but it is hard coded also

This will output a json output from the lambda

### Week 6
9/27/2023 Wk_6_s3_bucket_search.py
Run file with the following syntax 
    python Wk_6_s3_bucket_search.py -t <tag> -v <value>

    It will output bucket info matching the above and will write the contents of the bucket to a csv in that bucket.  It excludes other csv files.

### Week 8
10/25/2023 Wk_8_OOP
All files are in Wk_8_OOP Folder
    You can test code with pytest and Wk_8_OOP/object_oriented_test.py

### Week 9
11/8/2023 Wk_9_Res_Api
All Files are in the Wk_9_Res_Api Folder
    You can test using Wk_9_Rest_Api.py pytest

### Week 10
Pending: Vacation

### Week 11
Pending: COVID

### Week 12
12/13/2023 Wk_12
All Files are in the Wk_12 Folder
    Flask app is created by running Dynamo_Query_SQL.py file
    Pytest using Dynamo_Query_test.py

### Week 13
12/21/2023 Wk_13
All Files are in the Wk_13 Folder
    Flask app is created by running Dynamo_Query_SQL.py in Wk_13 folder
    Pytest is Dynamo_Query_test.pt in Wk_13 folder
    
### Environment

- training10

## References

- [SNS CLI]https://docs.aws.amazon.com/cli/latest/reference/sns/index.html#cli-aws-sns
- [Boto3 SNS]https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
- [Python Style Guide]https://peps.python.org/pep-0008/
- [reSt Style Guide]https://sweetpea-org.github.io/guide/contributing/rest_style_guide.html
- [Markdown Cheat Sheet]https://www.markdownguide.org/cheat-sheet/
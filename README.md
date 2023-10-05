# Code Bytes YOE

The Repo holds the code bytes files for each exercise

## Instructions

You will need to have a active saml2aws session to run these scripts

### 8/24/23 - 1_SNS Topic Search
Run file using the syntax: 
    python sns_topic_search.py --tag <tag> --key <name>
    use -h option for assistance

### 8/31/23 - 2_SSM Paramter Seach
Run file using the following syntax
    python ssm_parameter_search.py --tag1 <tag> --key1 <key_name_> --tag2 <tag> --key2 <key_name_>
    -h option will output format needed

### 9/6/2023 3_Bucket Output
Run file using the syntax:
    python bucket_search.py -f <filename>

Outputs to file in json format.  I feel like I missed something on this one because it was so little code.

### 9/14/2023 4_ EC2 Search and outputs
Run file with the following syntax 
    python 4_ec2_search.py -t <tag> -v <value>

    It will output instance info matching the above.  I did not test to see what happens with multiple instances having similar tags...It might be a nightmare.

**Search for key and values**
- example1: test1
- example2: test2
return name, type and value of parameter

### 9/20/2023 5_lambda_payload_response
Run file with the following syntax 
    python 5_lambda_payload_response.py -t <tag> -v <value>
    You can also include payload but it is hard coded also

This will output a json output from the lambda

### 9/27/2023 6_s3_bucket_search.py
Run file with the following syntax 
    python 6_s3_bucket_search.py -t <tag> -v <value>

    It will output bucket info matching the above and will write the contents of the bucket to a csv in that bucket.  It excludes other csv files.


### Environment

- training10

## References

- [SNS CLI]https://docs.aws.amazon.com/cli/latest/reference/sns/index.html#cli-aws-sns
- [Boto3 SNS]https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
- [Python Style Guide]https://peps.python.org/pep-0008/
- [reSt Style Guide]https://sweetpea-org.github.io/guide/contributing/rest_style_guide.html
- [Markdown Cheat Sheet]https://www.markdownguide.org/cheat-sheet/
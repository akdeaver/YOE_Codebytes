import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", dest='tag_key', help="Tag Key", required=True)
parser.add_argument("--value", dest='tag_value', help="Tag Value", required=True)

args = parser.parse_args()

print(f"Entered: {args.tag_key} {args.tag_value}")

#The process will bomb out if the required=True arguments aren't passed.  
#As far as your parameters go, I would have made 'Key' = User_key and 'Value' = User_value it took me a second to realize you swapped User_key with Value
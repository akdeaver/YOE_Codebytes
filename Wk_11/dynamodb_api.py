from boto3 import Session
import json
from wk_8 import Employee, Team

table_name = 'yoe-alex-teams'
session = Session(profile_name="training10", region_name="us-east-1")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table(table_name)
employees = []
teams = []

def team_check(team_name, team_id):
    try:
        response = table.get_item(Key={'team_id': team_id,'team_name':team_name})
        item = response.get('Item')
        if item:
            print(f"Team found")
        else:
            print(f"No team found with team_id '{team_id}' in DynamoDB.")
    except ClientError as e:
        print(f"Error reading team from DynamoDB: {e}")

def add_team(team_name, team_id):
    try:
        db_response = table.put_item(
            
            Item={
                'team_id': team_id,  # Convert team_id to int
                'team_name': team_name,
                'team_members': []  # Assuming 'team_members' is a list attribute
            },
            ConditionExpression='attribute_not_exists(team_id)'
        )
        print(f"Team '{team_name}' created in DynamoDB with team_id '{team_id}'")
        return team_id
    except ClientError as e:
        print(f"Error creating team in DynamoDB: {e}")
        return None


def remove_team():
    team_name = request.args.get('team_name')

    if team_name not in teams:
        return jsonify({"error": "team does not exist in array"}), 400
    else:
        teams.remove(team)
        return jsonify({"team": teams}), 200

def add_employees_to_team():
    test = 'nope'

def remove_employee_from_team():
    employee = "ted"

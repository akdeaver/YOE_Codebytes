from flask import Flask, jsonify, request
import psycopg2
import boto3
import os

aws_region = "us-east-1"
os.environ['AWS_PROFILE'] = "training10"

#Grabs ssm parameters needed to run query
#Thanks for brandon-m for the "['Parameter']['Value']" to shorten the number of lines
ssm = boto3.client('ssm', aws_region)
cluster_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/cluster', WithDecryption=True)['Parameter']['Value']
db_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/database', WithDecryption=True)['Parameter']['Value']
db_pw = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/password', WithDecryption=True)['Parameter']['Value']
db_uname = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/username', WithDecryption=True)['Parameter']['Value']

db_parameters = {
    'host': cluster_name,
    'database': db_name,
    'user': db_uname,
    'password': db_pw
}

def get_teams():
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_parameters)

        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT team_name FROM public.teams;")
        all_teams = cur.fetchall()

        cur.close()
        conn.close()

        result = [list for sublist in all_teams for list in sublist]
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def get_employees():
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_parameters)

        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT first_name, last_name, title, team_name FROM public.employees LEFT JOIN public.teams ON public.teams.id = public.employees.team_id;")
        result = cur.fetchall()

        cur.close()
        conn.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def get_teams_employees(team_name):
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_parameters)

        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT first_name, last_name, title, team_name FROM public.employees LEFT JOIN public.teams ON public.teams.id = public.employees.team_id WHERE team_name = %s", (team_name))
        result = cur.fetchall()

        cur.close()
        conn.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")


app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees_api():
    result = get_employees()
    return jsonify(result), 200

@app.route('/teams', methods=['GET'])
def get_teams_api():
    result = get_teams()
    return jsonify(result), 200

@app.route('/team', methods=['GET'])
def get_team_api():
    team_name = request.args.get('team_name')
    result = get_teams_employees(team_name)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(port=8000)
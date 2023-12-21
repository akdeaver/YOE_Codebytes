from flask import Flask, jsonify, request
import psycopg2
import boto3
import os

aws_region = "us-east-1"
os.environ['AWS_PROFILE'] = "training10"
'''
This week we needed to connect to a sql database.  
I wrote three different so I could get a list of all teams to get lists of each easily.
You can call /employees /teams /team?team_name={team_name}
'''

#Grabs ssm parameters needed to run query
ssm = boto3.client('ssm', aws_region)
cluster_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/cluster', WithDecryption=True)['Parameter']['Value']
db_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/database', WithDecryption=True)['Parameter']['Value']
db_pw = ssm.get_parameter(Name='/training10/techops/dsd/exercise13/alex', WithDecryption=True)['Parameter']['Value']
db_uname = "ex13_alex_rw"

db_parameters = {
    'host': cluster_name,
    'database': db_name,
    'user': db_uname,
    'password': db_pw
}

#Function to call out to get a list of team names from db
def get_teams():
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_parameters)
        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT team_name FROM public.ex13_alex_teams;")
        all_teams = cur.fetchall()

        #close connections
        cur.close()
        conn.close()

        #Converts list of lists to just single list
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
        cur.execute("SELECT first_name, last_name, title, team_name FROM public.ex13_alex_employees LEFT JOIN public.ex13_alex_teams ON public.ex13_alex_teams.id = public.ex13_alex_employees.team_id;")
        result = cur.fetchall()

        #Close connections and return result
        cur.close()
        conn.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def add_employee(first_name, last_name, title, team_name, date_of_birth, date_of_service):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)
    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        #Saving to improve in the future
        '''INSERT INTO table2 SELECT col1,col2 FROM table1 t1 WHERENOT EXISTS( SELECT 1 FROM table2 t2 WHERE t1.col1 = t2.col1 AND t1.col2 = t2.col2)'''

        #Query to find team id to match team name input
        team_id_query = "SELECT id FROM public.ex13_alex_teams WHERE team_name = %s;"
        cur.execute(team_id_query, (team_name,))
        team_id = cur.fetchone()

        #Query to insert new user
        insert_query = """
            INSERT INTO public.ex13_alex_employees (first_name, last_name, title, team_id, date_of_birth, date_of_service)
            VALUES (%s, %s, %s, %s, %s, %s);
        """

        # Execute the query
        cur.execute(insert_query, (first_name, last_name, title, team_id, date_of_birth, date_of_service))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        #Close connections and return result
        cur.close()
        conn.close()

def delete_employee(first_name, last_name):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)
    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        #Query to delete user when matches first name and last name
        sql = "Delete FROM public.ex13_alex_employees WHERE first_name = %s AND last_name = %s;"
        # Execute the query
        cur.execute(sql, (first_name, last_name))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        #Close connections and return result
        cur.close()
        conn.close()

def get_teams_employees(team_name):
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_parameters)

        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT first_name, last_name, title, team_name FROM public.ex13_alex_employees LEFT JOIN public.ex13_alex_teams ON public.ex13_alex_teams.id = public.ex13_alex_employees.team_id WHERE team_name = %s", (team_name,))
        result = cur.fetchall()

        #Close connections and return result
        cur.close()
        conn.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def remove_team(team_name):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)
    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        # Execute the query
        cur.execute("Delete FROM public.ex13_alex_teams WHERE team_name = %s", (team_name,))
        conn.commit()      

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        #Close connections and return result
        cur.close()
        conn.close()

def add_team(team_name):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)
    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        #Query to add team to values
        #Should check for existing first
        SQL = "INSERT INTO public.ex13_alex_teams (team_name) VALUES (%s);"
        data = (team_name,)
        # Execute the query
        cur.execute(SQL, data)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        #Close connections and return result
        cur.close()
        conn.close()

def update_team(old_team, team_name):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)
    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        #Query to update the team name to new name
        SQL = "UPDATE public.ex13_alex_teams SET team_name = %s WHERE team_name = %s;"
        data = (team_name, old_team)
        # Execute the query
        cur.execute(SQL, data)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        #Close connections and return result
        cur.close()
        conn.close()


#Flask App
app = Flask(__name__)

#App Route for /employees
@app.route('/employees', methods=['GET', 'POST', 'DELETE'])
def employees_api():
    if request.method == 'GET':
        #Run get get_employees definition to list all employees
        result = get_employees()

        #Form data from list of lists to json output
        json_result = [{"first_name": item[0], "last_name": item[1], "title": item[2], "team_name": item[3]} for item in result]
        return jsonify({"employees": json_result}), 200
    
    if request.method == 'POST':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        title = request.args.get('title')
        team_name = request.args.get('team_name')
        date_of_birth = request.args.get('date_of_birth')
        date_of_service = request.args.get('date_of_service')

        #Invoke add employee
        result = add_employee(first_name, last_name, title, team_name, date_of_birth, date_of_service)

        #Form data from list of lists to json output
        json_result = {"added": {"first_name": first_name, "last_name": last_name, "team_name": team_name }}
        return jsonify({"employee": json_result}), 200

    if request.method == 'DELETE':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        
        #invoke delete employee
        result = delete_employee(first_name, last_name)

        #Form data from list of lists to json output
        json_result = {"deleted": {"first_name": first_name, "last_name": last_name }}
        return jsonify({"employee": json_result}), 200

#App Route for /teams
@app.route('/teams', methods=['GET'])
def get_teams_api():
    #Run get_teams_api definition to list all teams
    result = get_teams()
    return result, 200

#App Route for /team
@app.route('/team', methods=['GET', 'DELETE', 'POST', 'PUT'])
def team_api():
    if request.method == 'GET':
        #Get team name input and run get_teams_employees definition
        team_name = request.args.get('team_name')
        result = get_teams_employees(team_name)

        #Form data from list of lists to json output
        json_result = [{"first_name": item[0], "last_name": item[1], "title": item[2]} for item in result]
        return jsonify({team_name : json_result}), 200
    
    if request.method == 'DELETE':
        #Take team name and remove from db
        team_name = request.args.get('team_name')
        result = remove_team(team_name)

        #Form data from list of lists to json output
        json_result = {"deleted": team_name }
        return jsonify({"team": json_result}), 200
    
    if request.method == 'POST':
        #take new team and add to db
        team_name = request.args.get('team_name')
        result = add_team(team_name)

        #Form data from list of lists to json output
        json_result = {"added": team_name }
        return jsonify({"team": json_result}), 200
    
    if request.method == 'PUT':
        #take new team and add to db
        team_name = request.args.get('team_name')
        old_team = request.args.get('old_team')
        result = update_team(old_team, team_name)

        #Form data from list of lists to json output
        json_result = {"updated": team_name }
        return jsonify({"team": json_result}), 200

if __name__ == '__main__':
    app.run(port=8000)
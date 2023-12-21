import boto3
import os
import psycopg2

aws_region = "us-east-1"
os.environ['AWS_PROFILE'] = "training10"
'''
This week we needed to connect to a sql database.  
I wrote three different so I could get a list of all teams to get lists of each easily.
You can call /employees /teams /team?team_name={team_name}
'''

#Grabs ssm parameters needed to run query
#Thanks for brandon-m for the "['Parameter']['Value']" to shorten the number of lines
ssm = boto3.client('ssm', aws_region)
cluster_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/cluster', WithDecryption=True)['Parameter']['Value']
db_name = ssm.get_parameter(Name='/training10/techops/dsd/exercise12/database', WithDecryption=True)['Parameter']['Value']
db_pw = ssm.get_parameter(Name='/training10/techops/dsd/exercise13/alex', WithDecryption=True)['Parameter']['Value']
db_uname = "ex13_alex_rw"

'''print(cluster_name)
print(db_name)
print(db_pw)
print(db_uname)'''

db_parameters = {
    'host': cluster_name,
    'database': db_name,
    'user': db_uname,
    'password': db_pw
}

#Function to call out to get a list of team names from db
'''def get_teams():
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


def add_team(team_name):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_parameters)

    # Create a cursor object to execute queries
    cur = conn.cursor()

    try:
        SQL = "INSERT INTO public.ex13_alex_teams (team_name) VALUES (%s);"
        data = (team_name,)
        # Execute the query
        cur.execute(SQL, data)
        #cur.execute("INSERT INTO public.ex13_alex_teams (team_name) VALUES %s", (team_name,))
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
        conn.close()'''

team_name = "Mainframe"
old_team = "DevOps"

'''print("Get Team Test")
result1 = get_teams()
print(result1)
print("Add DevOps Team")
result2 = add_team(team_name)
print(result2)
result3 = update_team(old_team, team_name)'''

first_name = "ted"
last_name = "logan"
title = "wild horse"
team = "Mainframe"
date_of_birth = "08/19/1985"
date_of_service = "04/01/2021"

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

result = get_employees()
print(result)
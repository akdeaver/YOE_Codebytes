from flask import Flask, jsonify, request
from wk_8 import Employee, Team

#https://emcins.atlassian.net/browse/COMENG-2221

app = Flask(__name__)

employees = []
teams = []

# Route to add and remove employees
@app.route('/employee', methods=['POST', 'DELETE'])
def employee():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    date_of_birth = request.args.get('date_of_birth')
    title = request.args.get('title')
    date_of_service = request.args.get('date_of_service')

    if request.method == 'POST': #self,fname,lname,title,dos
        employee = Employee(first_name,last_name,date_of_birth,title,date_of_service)

        '''for e in enumerate(employees):
            if (
                #print (employee)
                e.first_name == employee.first_name and e.last_name == employee.last_name
            ):
                return jsonify({'error': 'employee exists'}),  400'''
        employees.append(employee)
        return jsonify({'added': f"{employee.fname} {employee.lname}"}), 200
        
    if request.method == 'DELETE':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        
        for index, e in enumerate(employees):
            if (
                e.fname == first_name and e.lname == last_name
            ):
                employees.pop(index)
                return jsonify({'deleted': f"{e.fname} {e.lname}"}), 200
            return 'error: Employee not found', 404
        
# Route to get a list of all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    e = [f"{employee.lname}, {employee.fname}" for employee in employees]
    return jsonify({"employees": e}), 200

# Route to get details of a specific team
@app.route('/team', methods=['GET', 'POST', 'DELETE'])
def team():
    team_name = request.args.get('team_name')

    if request.method == 'POST':
        team = Team(team_name)

        '''if team_name in teams:
            return jsonify({"error": "team exists in array"}), 400
        else:
            teams.append(team)
            return jsonify({"team": team.team_name}), 200'''
        teams.append(team)
        return ({"team": teams}), 200
        
    ##Needs to be able to list team members
    elif request.method == 'GET':
        team_name = request.args.get('team_name')
        return team_name, 200

    elif request.method == 'DELETE':
        team_name = request.args.get('team_name')

        if team_name not in teams:
            return jsonify({"error": "team does not exist in array"}), 400
        else:
            teams.remove(team)
            return jsonify({"team": teams}), 200

# Route to get a list of all teams
##DONE needs comments
@app.route('/teams', methods=['GET'])
def get_teams():
    if len(teams) == 0:
        return jsonify({"error": "no teams in array"}), 400
    else:
        return jsonify({"teams": teams}), 200

@app.route('/team/members', methods=['POST', 'DELETE'])
def team_member():
    if request.method == 'POST':
        team_name = request.args.get('team_name')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')

        #index = find_team_index_by_name(team_name=team_name, teams=teams)
        for index, e in enumerate(employees):
            if (
                e.fname == first_name and e.lname == last_name
            ):
                return index
            return -1  

        if index < 0: 
            teams.append(Team(team_name))
        else:
            team = teams[index]

        #e_index = find_employee_index_by_name(first=first_name, last=last_name, employees=employees)
        for e_index, t in enumerate(teams):
            if (
                t.team_name == team_name
            ):
                return e_index
            return -1

        if e_index >= 0:
            team.add_employee(employees[e_index])
            return jsonify({'added': f"{first_name} {last_name}"})
        else:
            return jsonify({'error': 'employee not found'}), 404
        
    elif request.method == 'DELETE':
        return jsonify({'error': 'employee not found'}), 404

if __name__ == '__main__':
    app.run(port=8000)
from flask import Flask, jsonify, request
from person_employee import Person, Employee, Team

app = Flask(__name__)

employees = []
teams = []

def find_employee_index(employee, employees):
    for index, e in enumerate(employees):
        if (
            e.first_name == employee.first_name
            and e.last_name == employee.last_name
        ):
            return index
    return -1  

def find_employee_index_by_name(first, last, employees):
    for index, e in enumerate(employees):
        if (
            e.first_name == first
            and e.last_name == last
        ):
            return index
    return -1  

def find_team_index(team, teams):
    for index, t in enumerate(teams):
        if (
            t.team_name == team.team_name
        ):
            return index
    return -1    

def find_team_index_by_name(team_name, teams):
    for index, t in enumerate(teams):
        if (
            t.team_name == team_name
        ):
            return index
    return -1     

# Routes for Employee
@app.route('/employee', methods=['POST'])
def add_employee():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    date_of_birth = request.args.get('date_of_birth')
    title = request.args.get('title')
    date_of_service = request.args.get('date_of_service')

    employee = Employee(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, title=title, date_of_service=date_of_service)

    if find_employee_index(employee=employee, employees=employees) == -1:
        employees.append(employee)
        return jsonify({'added': f"{employee.first_name} {employee.last_name}"})
    else:
        return jsonify({'error': 'employee exists'}),  404

@app.route('/employee', methods=['DELETE'])
def delete_employee():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    index = find_employee_index_by_name(first=first_name, last=last_name,employees=employees)
    if index > -1:
        employee = employees[index]
        employees.pop(index)
        return jsonify({'deleted': f"{employee.first_name} {employee.last_name}"})
    else:
        return jsonify({'error': 'Employee not found'}),  404

@app.route('/employees', methods=['GET'])
def get_employees():
    e = [f"{employee.last_name}, {employee.first_name}" for employee in employees]
    return jsonify({'employees': e})

# Routes for Team
@app.route('/team', methods=['POST'])
def add_team():
    team_name = request.args.get('team_name')
    team = Team(team_name)
    
    if find_team_index(team=team, teams=teams) < 0:
        teams.append(team)
        return jsonify({'added': team.team_name})
    else: 
        return jsonify({'error': 'team exists'}),  404

@app.route('/team', methods=['DELETE'])
def delete_team():
    team_name = request.args.get('team_name')
    removed = False

    for team in teams:
        if team_name == team.team_name:
            teams.remove(team)
            removed = True

    if removed:
        return jsonify({'deleted': f"{team_name}"})
    else:
        return jsonify({'error': 'team not found'}), 404

@app.route('/team', methods=['GET'])
def get_team():
    team_name = request.args.get('team_name')
    index = find_team_index_by_name(team_name=team_name, teams=teams)
    
    if index >= 0:
        team = teams[index]
        members = [f"{employee.first_name} {employee.last_name}" for employee in team.employees]
        return jsonify({team.team_name: members})
    else:
        return jsonify({'error': 'Team not found'}), 404

# Routes for Team Members
@app.route('/team/members', methods=['POST'])
def add_team_member():
    team_name = request.args.get('team_name')
    index = find_team_index_by_name(team_name=team_name, teams=teams)

    if index < 0: 
        teams.append(Team(team_name))
    else:
        team = teams[index]

    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    e_index = find_employee_index_by_name(first=first_name, last=last_name, employees=employees)

    if e_index >= 0:
        team.add_employee(employees[e_index])
        return jsonify({'added': f"{first_name} {last_name}"})
    else:
        return jsonify({'error': 'employee not found'}), 404

@app.route('/team/members', methods=['DELETE'])
def remove_team_member():
    team_name = request.args.get('team_name')
    index = find_team_index_by_name(team_name=team_name, teams=teams)

    if index >= 0:
        team = teams[index]

        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        e_index = find_employee_index_by_name(first=first_name, last=last_name, employees=employees)

        if e_index >= 0:
            employee = employees[e_index]
            team.remove_employee(employee)
            return jsonify({'removed': f"{first_name} {last_name}"})
        else:
            return jsonify({'error': 'Employee not found'}), 404
    else:
        return jsonify({'error': 'Team not found'}), 404

# Route for listing all teams
@app.route('/teams', methods=['GET'])
def get_teams():
    teams_list = [] 
    for team in teams:
        teams_list.append(team.name)

    return jsonify({'teams': teams_list})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
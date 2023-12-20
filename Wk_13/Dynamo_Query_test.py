import pytest
import requests

base_url = "http://127.0.0.1:8000"
all_teams = [
    "Cloud Engineering",
    "Communication Engineering",
    "DevOps",
    "Mainframe",
    "Networking",
    "Site Reliability Engineering",
    "System Support Engineering"
]
all_employees =  [
    {"last_name": "ehlis", "first_name": "adam", "dob": "01/01/1975", "title": "Platform Engineering Manager", "team_name": "Cloud Engineering", "dos": "06/13/2020"},
    {"last_name": "botts", "first_name": "john", "dob": "12/01/1980", "title": "Platform Engineer III", "team_name": "Site Reliability Engineering", "dos": "06/13/2001"},
    {"last_name": "deaver", "first_name": "alex", "dob": "12/01/2000", "title": "Platform Engineer III", "team_name": "Communication Engineering", "dos": "08/01/2021"},
    {"last_name": "graber", "first_name": "mark", "dob": "09/01/1978", "title": "Senior Platform Engineer", "team_name": "Site Reliability Engineering", "dos": "03/01/2000"},
    {"last_name": "green", "first_name": "damien", "dob": "10/01/1981", "title": "Senior Network Engineer", "team_name": "Cloud Engineering", "dos": "10/01/2017"},
    {"last_name": "kolbe", "first_name": "scott", "dob": "10/01/1990", "title": "Network Engineer II", "team_name": "Networking", "dos": "06/01/2019"},
    {"last_name": "marcotte", "first_name": "brandon", "dob": "11/01/1989", "title": "Platform Engineer III", "team_name": "Communication Engineering", "dos": "08/01/2018"},
    {"last_name": "monroe", "first_name": "tiffany", "dob": "02/01/1998", "title": "System Support Engineer II", "team_name": "System Support Engineering", "dos": "12/01/2020"},
    {"last_name": "morris", "first_name": "tom", "dob": "02/01/1976", "title": "Platform Engineer III", "team_name": "Site Reliability Engineering", "dos": "02/01/2017"},
    {"last_name": "trujillo", "first_name": "michael", "dob": "05/01/1989", "title": "System Support Engineer II", "team_name": "System Support Engineering", "dos": "09/01/2018"},
    {"last_name": "walker", "first_name": "philip", "dob": "10/01/1965", "title": "Network Engineer II", "team_name": "Networking", "dos": "01/01/1995"}
]

def test_creating_teams_endpoint():
    for teams in all_teams:
        url = f"{base_url}/team?team_name={teams}"
        response = requests.post(url)

        #Assert the response status code is 200
        assert response.status_code == 200

def test_creating_employees_endpoint():
    for employee in all_employees:
        url = f"{base_url}/employees?last_name={employee['last_name']}&first_name={employee['first_name']}&date_of_birth={employee['dob']}&title={employee['title']}&team_name={employee['team_name']}&date_of_service={employee['dos']}"
        # Make the POST request
        response = requests.post(url)

        # Assert the response status code is 200
        assert response.status_code == 200

def test_employee_endpoint():
    url = f"{base_url}/employees"
    response = requests.get(url)

    #Assert the response status code is 200
    assert response.status_code == 200

def test_use_get_teams_for_list():
    url = f"{base_url}/teams"
    response = requests.get(url)
    print("testing teams")

    #Assert the response status code is 200
    assert response.status_code == 200

def test_get_team_endpoint():
    #Getting full list of teams for loop 
    url = f"{base_url}/teams"
    all_teams = requests.get(url).json()

    #Loop over teams and verify each is getting a 200
    for teams in all_teams:
        url = f"{base_url}/team?team_name={teams}"
        response = requests.get(url)

        #Assert the response status code is 200
        assert response.status_code == 200

#post cleanup when needed
def test_post_cleanup():
    for teams in all_teams:
        url = f"{base_url}/team?team_name={teams}"
        response = requests.delete(url)

        #Assert the response status code is 200
        assert response.status_code == 200

    for employee in all_employees:
        url = f"{base_url}/employees?last_name={employee['last_name']}&first_name={employee['first_name']}"
        response = requests.delete(url)

        #Assert the response status code is 200
        assert response.status_code == 200
import pytest
import requests

base_url = "http://127.0.0.1:8000"

def test_employee_endpoint():
    url = f"{base_url}/employees"
    response = requests.get(url)

    #Assert the response status code is 200
    assert response.status_code == 200

def use_get_teams_for_list():
    url = f"{base_url}/teams"
    response = requests.get(url)

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
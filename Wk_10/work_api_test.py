import pytest
import requests
from .wk_8 import Person, Employee, Team

base_url = "http://127.0.0.1:8000"
team_endpoint = "/team"
teams_endpoint = "/teams"
employee_endpoint = "/employee"
employees_endpoint = "/employees"
members_endpoint = "/members"

#Needed arrays
all_teams = {"Cloud Engineering", "Site Reliability Engineering", "Mainframe", "Networking", "Communication Engineering", "System Support Engineering"}
no_mainframe = {"Cloud Engineering", "Site Reliability Engineering", "Networking", "Communication Engineering", "System Support Engineering"}
employee_list = [
    {"lname": "ehlis", "fname": "adam", "dob": "01/01/1975", "t": "Platform Engineering Manager", "dos": "06/13/2020"},
    {"lname": "botts", "fname": "john", "dob": "12/01/1980", "t": "Platform Engineer III", "dos": "06/13/2001"},
    {"lname": "deaver", "fname": "alex", "dob": "12/01/2000", "t": "Platform Engineer III", "dos": "08/01/2021"},
    {"lname": "graber", "fname": "mark", "dob": "09/01/1978", "t": "Senior Platform Engineer", "dos": "03/01/2000"},
    {"lname": "green", "fname": "damien", "dob": "10/01/1981", "t": "Senior Network Engineer", "dos": "10/01/2017"},
    {"lname": "kolbe", "fname": "scott", "dob": "10/01/1990", "t": "Network Engineer II", "dos": "06/01/2019"},
    {"lname": "marcotte", "fname": "brandon", "dob": "11/01/1989", "t": "Platform Engineer III", "dos": "08/01/2018"},
    {"lname": "monroe", "fname": "tiffany", "dob": "02/01/1998", "t": "System Support Engineer II", "dos": "12/01/2020"},
    {"lname": "morris", "fname": "tom", "dob": "02/01/1976", "t": "Platform Engineer III", "dos": "02/01/2017"},
    {"lname": "trujillo", "fname": "michael", "dob": "05/01/1989", "t": "System Support Engineer II", "dos": "09/01/2018"},
    {"lname": "walker", "fname": "philip","dob": "10/01/1965", "t": "Network Engineer II", "dos": "01/01/1995"}
]
employee_list_minus = [
    {"lname": "botts", "fname": "john", "dob": "12/01/1980", "t": "Platform Engineer III", "dos": "06/13/2001"},
    {"lname": "deaver", "fname": "alex", "dob": "12/01/2000", "t": "Platform Engineer III", "dos": "08/01/2021"},
    {"lname": "graber", "fname": "mark", "dob": "09/01/1978", "t": "Senior Platform Engineer", "dos": "03/01/2000"},
    {"lname": "green", "fname": "damien", "dob": "10/01/1981", "t": "Senior Network Engineer", "dos": "10/01/2017"},
    {"lname": "kolbe", "fname": "scott", "dob": "10/01/1990", "t": "Network Engineer II", "dos": "06/01/2019"},
    {"lname": "marcotte", "fname": "brandon", "dob": "11/01/1989", "t": "Platform Engineer III", "dos": "08/01/2018"},
    {"lname": "monroe", "fname": "tiffany", "dob": "02/01/1998", "t": "System Support Engineer II", "dos": "12/01/2020"},
    {"lname": "morris", "fname": "tom", "dob": "02/01/1976", "t": "Platform Engineer III", "dos": "02/01/2017"},
    {"lname": "trujillo", "fname": "michael", "dob": "05/01/1989", "t": "System Support Engineer II", "dos": "09/01/2018"},
    {"lname": "walker", "fname": "philip","dob": "10/01/1965", "t": "Network Engineer II", "dos": "01/01/1995"}
]
team_list = [
    {"tname": "Site Reliability Engineering", "fname": "john", "lname": "botts"},
    {"tname": "Site Reliability Engineering", "fname": "tom", "lname": "morris"},
    {"tname": "Site Reliability Engineering", "fname": "mark", "lname": "graber"},
    {"tname": "Communication Engineering", "fname": "brandon", "lname": "marcotte"},
    {"tname": "Communication Engineering", "fname": "alex", "lname": "deaver"},
    {"tname": "System Support Engineering", "fname": "tiffany", "lname": "monroe"},
    {"tname": "System Support Engineering", "fname": "michael", "lname": "trujillo"},
    {"tname": "Networking", "fname": "scott", "lname": "kolbe"},
    {"tname": "Networking", "fname": "philip", "lname": "walker"},
    {"tname": "Cloud Engineering", "fname": "damien", "lname": "green"}
]

def test_post_team_endpoint():
    for teams in all_teams:
        url = f"{base_url}{team_endpoint}?team_name={teams}"
        # Make the POST request
        response = requests.post(url)

        # Assert the response status code is 200
        assert response.status_code == 200

'''def test_team_list_endpoint():
    url = f"{base_url}{teams_endpoint}"
    response = requests.get(url)

    assert response.status_code == 200
    ###assert response.json() == all_teams'''

'''def test_team_remove_endpoint():
    team_name = "Mainframe"
    url = f"{base_url}{team_endpoint}?team_name={team_name}"

    response = requests.delete(url)
    assert response.status_code == 200

    #Test 2
    url2 = f"{base_url}{teams_endpoint}"

    response2 = requests.get(url2)
    assert response2.status_code == 200
    ###assert response2.json() == no_mainframe'''

def test_employee_add_endpoint():  
    for employee in employee_list:
        url = f"{base_url}{employee_endpoint}?last_name={employee['lname']}&first_name={employee['fname']}&date_of_birth={employee['dob']}&title={employee['t']}&date_of_service={employee['dos']}"
        # Make the POST request
        response = requests.post(url)

        # Assert the response status code is 200
        assert response.status_code == 200

    url2 = f"{base_url}{employees_endpoint}"

    response = requests.get(url2)

    assert response.status_code == 200

def test_employee_delete_endpoint():
    lname = "ehlis"
    fname = "adam"
    url = f"{base_url}{employee_endpoint}?last_name={lname}&first_name={fname}"

    response = requests.delete(url)
    assert response.status_code == 200

    #Test 2
    #url2 = f"{base_url}{employees_endpoint}"

    #response2 = requests.get(url2)
    #assert response2.status.code == 200
    ###assert response2.json() == employee_list_minus

'''def test_team_member_add_endpoint():
    for team_member in team_list:
        url = f"{base_url}{team_endpoint}{members_endpoint}?team_name={team_member['tname']}&first_name={team_member['fname']}&last_name={team_member['lname']}"
        # Make the POST request
        response = requests.post(url)

        # Assert the response status code is 200
        assert response.status_code == 200'''

'''def test_team_list_endpoint():
    for teams in all_teams:
        url = f"{base_url}{team_endpoint}?team_name={teams}"
        response = requests.get(url)

        assert response.status_code == 200'''

'''def test_team_member_delete_endpoint():
    url = f"{base_url}{members_endpoint}?team_name=Site+Reliability+Engineering&first_name=john&last_name=botts"
    response = requests.delete(url)

    assert response.status_code == 200

    url2 = f"{base_url}{team_endpoint}?team_name=Site+Reliability+Engineering"
    response2 = requests.get(url2)

    assert response2.status_code == 200'''

if __name__ == "__main__":
    pytest.main([__file__])
import pytest
import requests
from .dynamodb_api import Person, Employee, Team

#Needed arrays
team_list = [
{"team_id": "1001", "team_name": "Cloud Engineering"},
{"team_id": "1002", "team_name": "Communication Engineering"},
{"team_id": "1003", "team_name": "DevOps"},
{"team_id": "1004", "team_name": "Mainframe"},
{"team_id": "1005", "team_name": "Networking"},
{"team_id": "1006", "team_name": "Site Reliability Engineering"},
{"team_id": "1007", "team_name": "System Support Engineering"} 
]
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

#Test for verifying name is outputted correctly
def test_add_team():
    
    assert person.full_name == "Kent Clark"

#Test for invalid creation of person class
def test_remove_team():
    with pytest.raises(ValueError):
        Person("Brandon","Marcotte","/12/1995")

#test for adding employees
def test_add_employees():
    team = Team()
    team.add_employee("Hawkeye")
    team.add_employee("Hulk")
    team.add_employee("Cap")
    team.add_employee("Widow")
    team_members = team.print_team()

    assert 'Hawkeye' in team_members
    assert 'Cap' in team_members
    assert 'Hulk' in team_members
    assert 'Widow' in team_members

#Test for removing members
def test_remove_employees():
    team = Team()
    team.add_employee("Hawkeye")
    team.add_employee("Hulk")
    team.add_employee("Cap")
    team.add_employee("Widow")
    team.remove_employee("Hulk")
    team_members = team.print_team()

    assert 'Hawkeye' in team_members
    assert 'Hulk' not in team_members    
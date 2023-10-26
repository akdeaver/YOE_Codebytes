import pytest
from datetime import datetime
from .object_oriented import Person, Employee, Team

#Test for verifying name is outputted correctly
def test_nameinput_shouldReturnName():
    person = Person("Clark","Kent","12/12/1978")
    assert person.full_name == "Kent Clark"

#Test for invalid creation of person class
def test_Person_date_shouldThrowError():
    with pytest.raises(ValueError):
        Person("Brandon","Marcotte","/12/1995")

#Test for invalid creation of Employee class
def test_Employee_date_shouldThrowError():
    with pytest.raises(ValueError):
        Employee("Brandon","Marcotte","Choas Engineer","/12/1995")

#Test for valid creation of Employee class
def test_Employee_date_shouldNotThrowError():
    '''
    Block of code because I don't know to generate another way'''
    time_format = "%m/%d/%Y"
    dos = "10/21/2023"
    today_datetime = datetime.today().strftime(time_format)
    today = datetime.strptime(today_datetime,time_format)
    start_day = datetime.strptime(dos,time_format)
    service_time = today - start_day
    time_in_service = service_time.days
    
    days = Employee("Gary","Snail","Cat","10/21/2023")
    assert days.time_in_service != 0
    assert days.time_in_service == time_in_service

#Test for valid creation of Employee class
#Today should always equal 0
#Testing others made the tests very large and duplicated the internal code
def test_Employee_date_shouldNotThrowError():
    time_format = "%m/%d/%Y"
    today = datetime.today().strftime(time_format)

    anniversary = Employee("Gary","Snail","Cat",today)
    assert anniversary.days_to_anniversay == 0

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
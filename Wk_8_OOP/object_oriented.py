from datetime import datetime

time_format = "%m/%d/%Y"

class Person:
    def __init__(self,fname,lname,birthdate):
        self.first_name = fname
        self.last_name = lname
        self.birthdate = birthdate
        self.full_name = ""
        self.birthdate_check()
        self.print_person_name()

    def birthdate_check(self):
        try:
            datetime.strptime(self.birthdate,time_format)
        except ValueError:
            raise ValueError("Invalid birthdate format, please match mm/dd/yyy")
        
    def print_person_name(self):
        self.full_name = self.last_name + " " + self.first_name
        print(self.full_name)

class Employee():
    def __init__(self,fname,lname,title,dos):
        self.title = title
        self.dos = dos
        self.time_in_service = 0
        self.days_to_anniversay = 10000

        #Converting the strftime to strptime formate as does not take the "time_format" correctly
        today_datetime = datetime.today().strftime(time_format)
        self.today = datetime.strptime(today_datetime,time_format)
        self.start_day = datetime.strptime(self.dos,time_format)

        self.date_check()
        self.service_time()
        self.milestone_anniversary()

    def date_check(self):
        try:
            datetime.strptime(self.dos,time_format)
        except ValueError:
            raise ValueError("Invalid date of service format, please match mm/dd/yyy")

    def service_time(self):
        service_time = self.today - self.start_day
        self.time_in_service = service_time.days
        return self.time_in_service

    def milestone_anniversary(self):
        years_to_milestone = 5 - ((self.today.year - self.start_day.year) % 5)

        if years_to_milestone % 5 != 0:
            milestone_year = years_to_milestone + self.today.year
        else:
            milestone_year = self.today.year

        milestone_anniversary = datetime(milestone_year, self.start_day.month, self.start_day.day)

        if self.today > milestone_anniversary:
            milestone_year = milestone_year + 5
            milestone_anniversary = datetime(milestone_year, self.start_day.month, self.start_day.day)

        temp_days_to_anniversay = milestone_anniversary - self.today
        self.days_to_anniversay = temp_days_to_anniversay.days
        print(self.days_to_anniversay)
        return self.days_to_anniversay


class Team():
    def __init__(self):
        self.team = []
        #self.member = member

    def add_employee(self,member):
        self.team.append(member)
        print(member)
        print(self.team)

    def remove_employee(self,member):
        if member in self.team:
            self.team.remove(member)
            print(member)
        else:
            raise AssertionError("Member does not exist in team")

    def print_team(self):
        return self.team
import pdpyras
import json

'''
This is as simple as I could make it.  This was made on my home computer due to difficulties but should work fine.

I will email my api_token and results.txt so that it is not share publically.

Additional notes below to explain process.
'''

api_token = 'in email'
service_name = 'AWS Budget' 

session = pdpyras.APISession(api_token)

#Get all user data
pd_users = session.iter_all('users')
pd_user_output = [{'user id': user['id'], 'username': user['name']} for user in pd_users]

#My user information
my_user = session.jget('/users/me')

#Get inputed service id information
for service in session.iter_all('services'):
    if service['name'] == service_name:
        service_id = service['id']

#Get service_name attributes
service_get = '/services/'+ service_id
service_attributes = session.jget(service_get)

#Search and print all incidents for given service_name
incidents = session.iter_all('incidents',params={'serivce_ids':[service_id]})
all_incidents = [{'incident id': incident['id'], 'last updated': incident['last_status_change_at'], 'incident title': incident['title']} for incident in incidents]

#write of all portions to results.txt
with open("results.txt", "w") as results_file:

    results_file.write("Return all users and their user id:\n")
    json.dump(pd_user_output, results_file, indent=4)
    results_file.write("\nMy user attributes:\n")
    json.dump(my_user, results_file, indent=4)
    results_file.write("\nAWS Budget Attributes:\n")
    json.dump(service_attributes, results_file, indent=4)
    results_file.write("\nIncidents for AWS Budget:\n")
    json.dump(all_incidents, results_file, indent=4)

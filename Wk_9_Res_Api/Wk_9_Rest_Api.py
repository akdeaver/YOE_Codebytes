'''
  This example uses the PDPYRAS library for Python
  https://github.com/PagerDuty/pdpyras
'''

from pdpyras import APISession

api_token = 'u+CTqsHbTQgYdyh6ibYQ'
session = APISession(api_token)

for user in session.iter_all('users'):
    print(user['id'])
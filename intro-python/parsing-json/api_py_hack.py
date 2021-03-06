#!/usr/bin/env python
"""make api call via py to see if I can do it"""

import requests
import json

# build request string
url = 'https://api.ciscospark.com/v1/teams'
header = {'Authorization' : 'Bearer NjlhZmE0Y2MtNmJkMC00ZjEyLWI5YmYtNDdkZTNjZmJiNzZjNWQ3MTI3MzctZTgy'}

# make request
r = requests.get(url, headers=header)

# I think the request comes back as a string so convert json text to json data
json_data = json.loads(r.text)

# print out each room name

print('\n')
for item in json_data["items"]:
    print(item["name"])
print('\n')

'''
generated via postman

import requests

url = "https://api.ciscospark.com/v1/teams"

headers = {
    'Authorization': "Bearer [MY KEY ID HERE]",
    'Cache-Control': "no-cache",
    'Postman-Token': "d03ab41e-6e96-4019-b74e-bf6ee39e21a3"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
'''

#!/usr/bin/env python
"""make api call via py to see if I can do it"""

import requests
import json

# build request string
url = 'https://api.ciscospark.com/v1/teams'
header = {'Authorization' : 'Bearer <redacted>'}

# make request
r = requests.get(url, headers=header)

# I think the request comes back as a string so convert json text to json data
json_data = json.loads(r.text)

# print out each room name

print('\n')
for item in json_data["items"]:
    print(item["name"])
print('\n')

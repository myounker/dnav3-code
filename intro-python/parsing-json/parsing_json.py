#!/usr/bin/env python
"""Parsing structured JSON text into native Python data structures...

...and how to access and work with nested data.
"""
""" code by myounker 1 Sep 2018 """


import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


# Read in the JSON text
with open(os.path.join(here, "interface-config.json")) as file:
    json_text = file.read()


# Display the type and contents of the json_text variable
print("json_text is a", type(json_text))
print(json_text)


# Use the json module to parse the JSON string into native Python data
json_data = json.loads(json_text)


# Display the type and contents of the json_data variable
print("json_data is a", type(json_data))
pprint(json_data)
#print(json_data)


# *** THIS CODE IS BROKEN *** The index into the datastruct doesn't work this way
#print('\n')
#print('with LOOP name ==>')
#for i in json_data["ietf-interfaces:interface"]["i"]:
#   print(i["name"])
# *** THIS CODE IS BROKEN *** The index into the datastruct doesn't work this way

print('with LOOP name ==>')
for i in json_data["ietf-interfaces:interface"]:
    print(json_data["ietf-interfaces:interface"][i])
    if json_data["ietf-interfaces:interface"][i] == "name":
        print(json_data["ietf-interfaces:interface"][i])
        print('foobar')

'''
print('\n')
print('with LOOP name ==>')
for i in json_data["ietf-interfaces:interface"]["name"]:
   print(i)
'''

print('\n')
print('without LOOP name ==>')
print(json_data["ietf-interfaces:interface"]["name"])

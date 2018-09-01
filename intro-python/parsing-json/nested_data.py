#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""
""" code by myounker 1 Sep 2018 """


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

#open file with interfaces and import text to variable called json_text
with open(os.path.join(here, "interfaces.json")) as file:
    json_text = file.read()

#put json string into py native format
json_data = json.loads(json_text)

# Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

print("\n")
for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"] + ': ' +
        interface["ietf-ip:ipv4"]["address"][0]["ip"] + ' ' +
        interface["ietf-ip:ipv4"]["address"][0]["netmask"]
        )
print("\n")

'''
solution on git used .format.  I need to learn that!!!
https://github.com/CiscoDevNet/dnav3-code/blob/solutions/intro-python/parsing-json/nested_data.py
print("{name}: {ip} {netmask}".format(
        name=interface["name"],
        ip=interface["ietf-ip:ipv4"]["address"][0]["ip"],
        netmask=interface["ietf-ip:ipv4"]["address"][0]["netmask"],

'''

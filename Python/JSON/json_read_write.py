#!/usr/bin/python
import json
import os
from pprint import pprint

with open(os.getcwd() + '/Python/JSON/data2.json', "r") as file:
    json_content = json.load(file)

# file = open(os.getcwd() + '/Python/JSON/data2.json')

pprint(json_content, indent=2)
print('\n')
# print(json_content.keys())
# print('\n')
# print(json_content.items())
# print('\n')
# print(json_content.values())
# print('\n')

print(json_content['children'][0]['firstName'])

file.close()

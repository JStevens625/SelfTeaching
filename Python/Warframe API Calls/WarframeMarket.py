#!/usr/bin/python3

import requests
import os
import json

response = requests.get('https://api.warframestat.us')

print(response.json())

#!/usr/bin/python3

import requests
import http.client, urllib

#My Version
Custom Made API Posting
payload = {
    'user': 'USER TOKEN',
    'token': 'API TOKEN',
    'message': "Hello World!"
}
response = requests.post('https://api.pushover.net:443/1/messages.json', params=payload)

#Official API posting!
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    'user': 'USER TOKEN',
    'token': 'API TOKEN',
    'message': "Hello World!"
  }),
  {"Content-type": "application/x-www-form-urlencoded"})
conn.getresponse()

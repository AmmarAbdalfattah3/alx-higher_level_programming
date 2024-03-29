#!/usr/bin/python3
"""This Python script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as
   a parameter, and displays the body of the response
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    par = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=par, method='POST')

    with urllib.request.urlopen(request) as response:
        body_response = response.read().decode('utf-8')
        print(body_response)

#!/usr/bin/python3
"""This Python script that takes in a URL, sends a request to
   the URL and displays the value of the variable
   X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response_header = requests.get(url)

    if 'X-Request-Id' in response_header.headers:
        print(response_header.headers['X-Request-Id'])

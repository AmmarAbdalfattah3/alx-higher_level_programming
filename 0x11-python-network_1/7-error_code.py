#!/usr/bin/python3
"""This Python script that takes in a URL, sends a request
   to the URL and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    body_response = requests.get(url)

    if body_response.status_code >= 400:
        print(f"Error code: {body_response.status_code}")
    else:
        print(body_response.text)

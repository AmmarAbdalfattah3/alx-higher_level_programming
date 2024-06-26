#!/usr/bin/python3
"""This Python script that fetches https://alx-intranet.hbtn.io/status
   using the package requests
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

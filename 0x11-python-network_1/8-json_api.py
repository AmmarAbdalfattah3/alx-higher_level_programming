#!/usr/bin/python3
""" a Python script that takes in a letter and sends
    a POST request to http://0.0.0.0:5000/search_use
    with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    data = {"q": letter}
    res = requests.post(url, data=data)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")

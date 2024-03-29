#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    body_response = requests.post(url, data={"q": letter})

    try:
        data = body_response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
   to the URL and displays the body of the response
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            body_response = res.read().decode('utf-8')
            print(body_response)

    except urllib.error.HTTPError as err:
        print("Error code:", err.code)

#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
	sends a POST request to the passed URL with the email
	as a parameter, and displays the body of the
	response (decoded in utf-8)
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
	url = url = sys.argv[1]
	data = {"email": sys.argv[2]}
	data = parse.urlencode(data)
	data = data.encode("ascii")
	request = request.Request(url, data)
	with request.urlopen(request) as res:
		result = res.read()
		print(result.decode("UTF-8"))
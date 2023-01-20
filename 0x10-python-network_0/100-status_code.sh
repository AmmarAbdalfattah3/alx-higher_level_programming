#!/bin/bash
# takes in a URL, sends a req to it and displays the status code of res
curl -s -o /dev/null -w "%{http_code}" "$1"

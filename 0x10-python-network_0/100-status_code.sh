#!/bin/bash
#This Bash script that sends a request to a URL and displays the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"

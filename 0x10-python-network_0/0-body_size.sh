#!/bin/bash
# takes in a URL, sends a req to that URL and displays the res body size
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2

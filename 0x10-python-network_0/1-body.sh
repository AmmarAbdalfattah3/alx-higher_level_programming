#!/bin/bash
# takes in a URL , sends a GET req to it and displays the body of res
curl -fs -L "$1" -X GET

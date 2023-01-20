#!/bin/bash
# sends a json post req and displays the body of res
curl -sL -H "content-type:application/json" -d @"$2" "$1" -X POST

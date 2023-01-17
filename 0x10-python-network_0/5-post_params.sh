#!/bin/bash
# takes in a URL, sends a POST req to it and displays the body of res
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST

#!/bin/bash
#This BASH script takes in a URL, sends a POST request to the passed URL
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST

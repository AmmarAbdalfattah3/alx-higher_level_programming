#!/bin/bash
# takes in a URL, send a DELETE req to it and displays the body of res
curl -sfL "$1" -X DELETE

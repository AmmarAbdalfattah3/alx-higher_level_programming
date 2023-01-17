#!/bin/bash
# takes in a url, sends a GET req to it and displays the body of res
curl -sH "X-School-User-Id: 98" "$1"

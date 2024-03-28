#!/bin/bash
# makes an HTTP req to 0.0.0.0:5000/catch_me making the server respond with "you got me!""
curl -sL -d "user_id=98" -H "origin: HolbertonSchool" 0.0.0.0:5000/catch_me -X PUT

#!/bin/bash
# Bash script that makes a request that causes the server to respond with a message
curl -sL -X PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

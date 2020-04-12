#!/bin/bash
#script that makes a request that causes the server to respond with a message
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"

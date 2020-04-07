#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"

#!/usr/bin/python3
'''
script that takes in a URL and an email address,
sends a POST request to the passed URL
'''


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    param = {'email': sys.argv[2]}
    r = requests.post(url, data=param)
    print(r.text)
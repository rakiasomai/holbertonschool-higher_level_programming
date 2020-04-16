#!/usr/bin/python3
'''
script that takes in a URL and an email, sends a POST request to the passed URL
'''
from sys import argv
import urllib.request
import urllib.parse
if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

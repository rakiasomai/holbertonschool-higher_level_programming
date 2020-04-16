#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
and displays the value of the variable
'''
import sys
import requests

if __name__ == "__main__":
    urll = sys.argv[1]
    r = requests.get(urll)
    print(r.headers['X-Request-Id'])

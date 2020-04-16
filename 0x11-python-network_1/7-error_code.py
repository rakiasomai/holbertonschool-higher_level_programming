#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
and displays the body of the response.
'''


import sys
import requests

if __name__ == "__main__":
    urll = sys.argv[1]
    r = requests.get(urll)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))

#!/usr/bin/python3
# Python script that fetches


import requests

if __name__ == "__main__":
    urll = "https://intranet.hbtn.io/status"
    r = requests.get(urll)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

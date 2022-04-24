#!/usr/bin/python3
""" 2. POST an email #0 """
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as response:
        print("{}".format(response.read().decode("utf-8")))

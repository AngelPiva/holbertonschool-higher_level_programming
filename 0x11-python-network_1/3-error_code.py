#!/usr/bin/python3
""" 3. Error code #0 """
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print("{}".format(response.read().decode("utf-8")))
    except urllib.error.HTTPError as exception:
        print("Error code: {}".format(exception.code))

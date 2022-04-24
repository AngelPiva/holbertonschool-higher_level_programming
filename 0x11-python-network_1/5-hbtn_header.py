#!/usr/bin/python3
""" 5. Response header value #1 """
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print("{}".format(r.headers.get("X-Request-Id")))

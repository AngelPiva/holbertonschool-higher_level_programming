#!/usr/bin/python3
""" Response header value #0 """
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        req_id = response.info().get("X-Request-Id")
        print(req_id)

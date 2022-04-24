#!/usr/bin/python3
""" 9. My GitHub! """
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=(argv[1], argv[2])).json()
    print(r.get("id"))

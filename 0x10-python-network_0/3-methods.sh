#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI "http://$1" | grep "Allow" | cut -d" " --fields=2,3,4

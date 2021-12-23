#!/usr/bin/python3
import hidden_4
elements = dir(hidden_4)
for i in elements:
    if i[:2] != '__':
        print('{}'.format(i))

#!/usr/bin/python3
n = 0
for i in reversed(range(97, 123)):
    print('{:c}'.format(i - n), end='')
    if n == 0:
        n = 32
    else:
        n = 0

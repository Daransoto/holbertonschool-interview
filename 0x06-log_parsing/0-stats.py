#!/usr/bin/python3
"""
This script parses logs.
"""
import sys


res = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
       "405": 0, "500": 0}
size = 0
try:
    for i, logs in enumerate(sys.stdin, 1):
        if logs.split(' ')[7] not in res.keys():
            continue
        res[logs.split(' ')[7]] += 1
        size += int(logs.split(' ')[8])
        if i % 10 == 0:
            print("{}: {:d}".format("File size", size))
            for key, value in sorted(res.items()):
                if value > 0:
                    print("{}: {:d}".format(key, value))
finally:
    print("{}: {:d}".format("File size", size))
    for key, value in sorted(res.items()):
        if value > 0:
            print("{}: {:d}".format(key, value))

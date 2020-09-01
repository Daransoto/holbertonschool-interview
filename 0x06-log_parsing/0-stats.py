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
        data = logs.split()
        if len(data) > 2:
            size += int(data[-1])
            if data[-2] in res.keys():
                res[data[-2]] += 1
            if i % 10 == 0:
                print("{}: {}".format("File size", size))
                for key in sorted(res.keys()):
                    if res[key] != 0:
                        print("{}: {}".format(key, res[key]))
finally:
    print("{}: {}".format("File size", size))
    for key in sorted(res.keys()):
        if res[key] != 0:
            print("{}: {}".format(key, res[key]))

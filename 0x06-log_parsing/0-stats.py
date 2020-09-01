#!/usr/bin/python3
"""
This script parses logs.
"""


res = {"size": 0, "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
       "405": 0, "500": 0}
i = 0
while True:
    try:
        i += 1
        logs = input()
        if logs.split(' ')[7] not in res.keys():
            continue
        res[logs.split(' ')[7]] += 1
        res["size"] += int(logs.split(' ')[8])
        if i % 10 == 0:
            print("{}: {:d}".format("File size", res["size"]))
            for key, value in sorted(res.items()):
                if value > 0 and key != "size":
                    print("{}: {:d}".format(key, value))
    except:
        print("{}: {:d}".format("File size", res["size"]))
        for key, value in sorted(res.items()):
            if value > 0 and key != "size":
                print("{}: {:d}".format(key, value))
        break

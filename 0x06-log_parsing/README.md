# 0x06. Log Parsing

##

### Description

This project is about writing a script that computes metrics from logs.<br>
Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`<br>
After every 10 lines and/or a keyboard interruption (CTRL + C), prints these statistics from the beginning:<br>
`Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
format: <status code>: <number>
status codes are printed in ascending order`

### Mandatory Tasks

| File | Description |
| ------ | ------ |
| [0-stats.py](0-stats.py) | Reads stdin line by line and computes metrics. |


## Author

[Darwin Soto](https://twitter.com/darutos)

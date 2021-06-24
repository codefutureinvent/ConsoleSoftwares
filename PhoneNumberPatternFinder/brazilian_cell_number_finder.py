#!/usr/bin/env python

import re
import subprocess

WHITE = '\u001b[37m'
RED = '\u001b[31m'

subprocess.call('clear')
user_input = input('Enter your text: ')
result = re.findall(r'\d\d-\d\d\d\d\d-\d\d\d\d', user_input)

if not any(result):
    print(RED, 'No Number Found!', sep='')
else:
    for position, number in enumerate(result):
        print(RED, position + 1, end='', sep='')
        print(WHITE, number, sep=': ')

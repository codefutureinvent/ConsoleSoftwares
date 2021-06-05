#!/usr/bin/env python3

###########################
# Version: 1.0.0          #
# Author: Victor Kolis    #
###########################

from pathlib import Path
import platform
import requests
import time
import sys
import os
import re

# Global variables
YELLOW = '\u001b[34m'
GREEN = '\u001b[32m'
RED = '\u001b[31m'

res = requests.get('https://google.com/search?q=weather')

# Operating system terminal clearing command
unknown = '*'
commands = {
    'Linux': 'clear',
    'Darwin': 'clear',
    'Windows': 'cls',
    unknown: 'Sorry, we do not work with this OS.'
}

# Operating System validation
op_system = platform.system()
try:
    commands[op_system]
except KeyError:
    print(RED, commands[unknown])
    time.sleep(5)
    sys.exit()


def clear():
    os.system(commands[op_system])


clear()
print(YELLOW, 'Welcome To The Weather Grabber Console App')
year = time.ctime().split()[-1]
month = time.ctime().split()[1]
day = time.ctime().split()[2]

# Saving page request
f = open('webpage.txt', 'w')
f.write(res.text)

file_text = Path('webpage.txt').read_text()
city_compiler = re.compile(r'weather for \w+')
mo = city_compiler.search(file_text)

temperature = re.findall(r'\d\d°\w', file_text)

try:
    print(GREEN, f'{mo.group().title()} - {temperature[0]}')
except AttributeError:
    print(RED, 'No city was found!')

print(GREEN, '{}/{}/{}'.format(month, day, year))

f.close()

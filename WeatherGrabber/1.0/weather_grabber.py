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

# Global variables for ascii colors
BLUE = '\u001b[34m'
GREEN = '\u001b[32m'
RED = '\u001b[31m'

# OS commands
commands = {
    'Linux': 'clear',
    'Darwin': 'clear',
    'Windows': 'cls',
}


def clear():
    """ Operates a prompt script according to the user's operating system """
    os.system(commands[op_system])


# OS validation
op_system = platform.system()
if not commands.get(op_system):
    print(RED, 'We do not support this operating system yet.')
    time.sleep(5)
    sys.exit()

# Getting and saving request
req_response = requests.get('https://google.com/search?q=weather')
collected_html = 'webpage.txt'
f = open(collected_html, 'w')
f.write(req_response.text)

# Reading the html from the file
file_text = Path(collected_html).read_text()
city_compiler = re.compile(r'weather for \w+')
mo = city_compiler.search(file_text)
temperature = re.findall(r'\d+°\w', file_text)

# Software intro
clear()
print(BLUE, 'Welcome To The Weather Grabber Console App')
year = time.ctime().split()[-1]
month = time.ctime().split()[1]
day = time.ctime().split()[2]

try:
    print(GREEN, f'{mo.group().title()} - {temperature[0]}')
except AttributeError:
    print(RED, 'No city was found!')
    sys.exit()
print(GREEN, '{}/{}/{}'.format(month, day, year))

current_time = re.findall(r'\d\d:\d\d:\d\d', time.ctime())
print('',*current_time, sep=' ')

f.close()

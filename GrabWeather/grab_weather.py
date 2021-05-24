#!/usr/bin/env python3

###########################
# Version: 1.0.0          #
# Author: Victor Kolis    #
###########################

from datetime import date
import platform
import requests
import time
import sys
import os
import re

# Global variables
YELLOW = '\u001b[33m'
GREEN = '\u001b[32m'
RED = '\u001b[31m'

res = requests.get('https://google.com/search?q=weather')
res.raise_for_status()

text = '''
"BNeawe tAd8D AP7Wnd">Jundiaí - Aglomeração Urbana de Jundiaí, Jundiaí - SP
</span></span><span class="BNeawe s3v9rd AP7Wnd"> / </span><span><span class=
"BNeawe s3v9rd AP7Wnd">Clima</span></span></div><div class="Q0HXG"></div><div><div><div><div class="kCrYT"><div class="lnWbdd"><div class="kvKEAb"><div><div><div class="BNeawe iBp4i AP7Wnd"><div><div class="
BNeawe iBp4i AP7Wnd">17°C</div></div></div></div></div><div><div><div class="BNeawe tAd8D AP7Wnd"><div><div class="
BNeawe tAd8D AP7Wnd">domingo 07:16 Nublado<
'''



commands = {
    'Linux': 'clear',
    'Darwin': 'clear',
    'Windows': 'cls',
    'Unknown': 'Sorry, we do not work with this OS.'
}

# Operating System validation
op_system = platform.system()
try:
    commands[op_system]
except KeyError:
    print(RED, commands['Unknown'])
    time.sleep(5)
    sys.exit()


def clear():
    os.system(command)


print(YELLOW, 'Welcome To The Weather Grabber Console App')
# TODO: Grab the name of the city wholly
year, month, day = str(date.today()).split('-')

# Months namely
months = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

print(GREEN, time.ctime())

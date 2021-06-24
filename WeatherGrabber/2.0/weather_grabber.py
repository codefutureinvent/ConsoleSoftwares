#!/usr/bin/env python3

from selenium import webdriver
import os, sys, platform, time


def clear():
    commands = {
        'Linux': 'clear',
        'Darwin': 'clear',
        'Windows': 'cls'
    }
    os.system(commands.get(platform.system()))


# Getting the user's input
clear()
print('Welcome to the Weather Grabber 2.0')
user_input = input('Enter your location, or just hit enter to get you current location: ')

# Getting the weather info
browser = webdriver.Firefox()
url = 'https://www.google.com/search?channel=fs&client=ubuntu&q=weather{}'
browser.get(url.format(f' {user_input}' if user_input else ''))

# Getting the css selectors texts
temp_in_number = int(browser.find_element_by_css_selector('#wob_tm').text)
rain = browser.find_element_by_css_selector('.wtsRwe > div:nth-child(1)').text
humidity = browser.find_element_by_css_selector('.wtsRwe > div:nth-child(2)').text
wind = browser.find_element_by_css_selector('.wtsRwe > div:nth-child(3)').text
city_name = browser.find_element_by_css_selector('#wob_loc').text
weather = browser.find_element_by_css_selector('#wob_dcp').text
browser.quit()

# Getting the current day
year = time.ctime().split()[-1]
month = time.ctime().split()[1]
day = time.ctime().split()[2]

# Displaying info
print(f'{city_name.title()} -- {temp_in_number}°C | {temp_in_number * 1.8 + 32:.2f}°F')
print(f'{month}/{day}/{year}')
print(f'{rain}')
print(f'{humidity}')
print(f'{wind}')

# Text distancing
for i in range(10):
    print()

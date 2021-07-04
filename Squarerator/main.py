#!/usr/bin/env python3

# Author: Victor Kolis
# Version: 1.0.0
# Supported OS: Debian unix systems

"""
This is a software that creates squares out of characters you wish.
Its goals is to save you the creator some time on making such ascii art.
Down below a representation of the software standard output is shown:

* * * *
*     *
*     *
* * * *
"""

import sys
from os import system
from time import sleep

# Variables & Constants: enum
greeting = 'Welcome to Squarerator the square creator software.\nVersion 1.0.0 by Kolis\n'
help = 'Welcome to Squarerator help guide menu.\
\nYou must needs to set the size of the square and its symbol plus separator.\
The size must needs be an int and the others printable characters.'
command = 'clear'
sleep_time = 0.05


class Enum:
    FIRST_LAST_ROW = 2


def squarerator(size: int, figure: str, separator: str) -> str:
    size = abs(size)
    figure = figure if figure else '*'
    separator = separator if separator else ' '
    first_last_row = figure + (separator + figure) * (size - 1)
    rows = f'{figure + separator * (size + (size - 1) - 2)}{figure}\n'
    square = f'{first_last_row}\n'
    for i in range(size - Enum.FIRST_LAST_ROW):
        square += rows
    square += first_last_row
    return square if size > 1 else figure if size != 0 else ''


system('clear')
for i in greeting:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(sleep_time)


while True:
    try:
        square_size = int(input('Square size |: '))
        if square_size == 0:
            system(command)
            for i in help:
                sys.stdout.write(i)
                sys.stdout.flush()
                sleep(sleep_time)
            sleep(4)
            system(command)
            continue
        character = input('Square symbol |: ')
        char_separator = input('Symbol separator |: ')
        system(command)
        print(squarerator(square_size, character, char_separator))
        break
    except ValueError:
        system(command)
        sys.stderr.write('Enter and integer or float for the square size!\n')

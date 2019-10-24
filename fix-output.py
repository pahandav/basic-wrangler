#!/usr/bin/env python3
""" fix-output.py - Helper script that fixes C64List output for BASIC Wrangler.

c64list <filename> -lbl

fix-output <filename>.lbl

Outputs as <filename>.lbn """

import re
import sys

RE_QUOTES = r'(?=([^"]*"[^"]*")*[^"]*$)'
FILENAME = sys.argv[1]

with open(FILENAME) as file:
    input_file = file.readlines()

for index, line in enumerate(input_file):
    input_file[index] = input_file[index].lstrip()
    input_file[index] = input_file[index].replace('{:', '`')
    input_file[index] = input_file[index].replace('}', '')
    # This replaces every REM not in quotes with an apostrophe
    input_file[index] = re.sub('REM' + RE_QUOTES, '\'', input_file[index])

with open(FILENAME[0:-4] + '.lbn', 'w') as file:
    file.writelines(input_file)

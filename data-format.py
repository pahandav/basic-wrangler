#!/usr/bin/env python3
""" data-format.py - Helper script that fixes C64List output for BASIC Wrangler.

data-format <filename>

Outputs as <filename>.dat """

import re
import sys

RE_QUOTES = r'(?=([^"]*"[^"]*")*[^"]*$)'
FILENAME = sys.argv[1]

with open(FILENAME) as file:
    input_file = file.readlines()

data_statement = '#data\n'

for index, line in enumerate(input_file):
    if line.startswith('DATA'):
        stripped = line.lstrip('DATA')
        # This replaces every comma in between data statement values not in quotes with a newline
        temp = re.sub(',' + RE_QUOTES, '\n', stripped)
        temp = temp.lstrip()
        data_statement = data_statement + temp
        input_file[index] = ''

data_statement = data_statement + '#enddata\n'

final = list(filter(None, input_file))

final.append(data_statement)

with open(FILENAME[0:-4] + '.dat', 'w') as file:
    file.writelines(final)

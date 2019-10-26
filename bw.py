#!/usr/bin/env python3
""" basic-wrangler - A BASIC program listing line renumberer/cruncher. """

import argparse
import json
import logging
import re
import sys
from collections import namedtuple
from pathlib import Path

import pyperclip

import basdefs

# constants
RE_QUOTES = r'(?=([^"]*"[^"]*")*[^"]*$)' # this selects things NOT inside quotes
ALWAYS_FILE_FORMAT = ['bascom', 'amiga', 'riscos', 'gwbasic']
CBM_BASIC = ['pet', 'vic20', 'c64', 'plus4', 'c128']

def reformat_data_statements(input_file, basic_defs):
    """ Formats a newline-delimited list of values into DATA statements.

    TODO: Improve this function, I'm amazed it works at all right now. """
    if basic_defs.data_length is None:
        data_statement_length = basic_defs.basic_line_length - 9
    elif basic_defs.data_length is not None:
        data_statement_length = basic_defs.data_length - 9
    output_file = list()
    for index, line in enumerate(input_file):
        if line.startswith('#data'):
            start_data_block = index + 1
            break
        else:
            output_file.append(line)
    for index, line in enumerate(input_file):
        if line.startswith('#enddata'):
            end_data_block = index
    data_block = list()
    for index in range(start_data_block, end_data_block):
        data_block.append(input_file[index])
    logging.debug(data_block)
    need_new_data_statement = True
    data_statement = ''
    for index, line in enumerate(data_block):
        if need_new_data_statement:
            data_statement = 'DATA ' + line + ','
            logging.debug(data_statement)
            need_new_data_statement = False
            continue
        if len(data_statement) + len(line) > data_statement_length:
            need_new_data_statement = True
            data_statement = data_statement + line
            output_file.append(data_statement)
            logging.debug(data_statement)
            data_statement = ''
            continue
        data_statement = data_statement + line + ','
        logging.debug(data_statement)
    data_statement = data_statement.rstrip(',')
    logging.debug(data_statement)
    output_file.append(data_statement)
    output_file = list(filter(None, output_file))
    return output_file

def fix_spacing(line):
    """ Removes spaces where they are not needed. """
    error_list = [('"', ';'), (';', '"'), ('<>', '"'), ('=', '"')]
    adjust_length = 0
    # remove spaces between one thing and another using the list of tuples above
    for index, _ in enumerate(error_list):
        for x in range(len(line)-1, -1, -1):
            if line[x-1].endswith(error_list[index][0]) and line[x].startswith(error_list[index][1]):
                line[x-1] = line[x-1] + line[x]
                line.pop(x)
                adjust_length += 1
    # remove spaces between comma joined elements
    for x in range(len(line)-1, -1, -1):
        if line[x] == ',':
            line[x-1] = line[x-1] + line[x] + line[x+1]
            line.pop(x+1)
            line.pop(x)
            adjust_length += 2
    logging.debug('Line adjusment is: %s', adjust_length)
    return line, adjust_length

def check_new_line(line):
    """ Checks to see if a new line is mandatory. """
    need_new_line = False
    if 'IF' in line: need_new_line = True
    if 'GOTO' in line: need_new_line = True
    if 'RETURN' in line: need_new_line = True
    if 'DATA' in line: need_new_line = True
    if 'D.' in line: need_new_line = True
    if 'REM' in line: need_new_line = True
    return need_new_line

def determine_line_length(line, basic_defs, line_replacement):
    """ Algorithmically determine the length of a line. """
    current_line_length = 0
    for element in line:
        if element.startswith('`'):
            current_line_length = current_line_length + line_replacement
        elif element == 'PRINT' and basic_defs.print_as_question:
            current_line_length += 1
        else:
            current_line_length = current_line_length + len(element)
    if basic_defs.crunch == 0:
        for element in line:
            current_line_length += 1
    return current_line_length

def crunch_line(line, basic_defs):
    """ This function crunches lines.

    If crunch is 0, it will join with spaces, and if crunch is 1 it will join with no spaces. """
    if not basic_defs.tokenize:
        while basic_defs.print_as_question and 'PRINT' in line:
            print_index = line.index('PRINT')
            line[print_index] = '?'
    if basic_defs.crunch == 1:
        final_line = ''.join(line)
    else:
        final_line = ' '.join(line)
    return final_line

def tokenize_line(line):
    """ A super-naive line lexer.

    This splits a string on spaces, quotes, and commas to create a list of tokens.
    TODO: replace this with a better lexer at some point. """
    temp1 = re.split(r'(\s|\".*?\"|,)', line)
    temp2 = [x for x in temp1 if x.strip()]
    return temp2

def start_new_line(current_line_number):
    """ Starts a new BASIC line. """
    current_line = str(current_line_number)
    current_line_length = len(current_line)
    return current_line, current_line_length

def renumber_basic_file(input_file, basic_defs, label_dict, line_replacement, basic_type):
    """ The main renumbering routine. """
    output_file = list()
    current_line_number = basic_defs.numbering
    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
    for line in input_file:
        logging.debug(persistent_buffer)
        # routine for jump targets
        if line.startswith('`'):
            if persistent_buffer != str(current_line_number):
                label_dict[line] = current_line_number + basic_defs.increment
                persistent_buffer = persistent_buffer.rstrip(basic_defs.statement_joining_character)
                output_file.append(persistent_buffer)
                current_line_number = current_line_number + basic_defs.increment
            else:
                label_dict[line] = current_line_number
            logging.debug(persistent_buffer)
            persistent_buffer, persistent_line_length = start_new_line(current_line_number)
            continue
        # tokenizes lines, determines line length, and sets the current buffer to the tokenized line
        tokenized_line = tokenize_line(line)
        logging.debug(tokenized_line)
        current_buffer_length = determine_line_length(tokenized_line, basic_defs, line_replacement)
        logging.debug('Current buffer length: %s', current_buffer_length)
        # fix spacing when spaces are needed
        if basic_defs.crunch != 1:
            fixed_line, adjust_length = fix_spacing(tokenized_line)
            current_buffer_length = current_buffer_length - adjust_length
            current_buffer = crunch_line(fixed_line, basic_defs)
        else:
            current_buffer = crunch_line(tokenized_line, basic_defs)
        logging.debug(current_buffer)
        # when lines don't need to be combined
        if not basic_defs.combine:
            persistent_buffer = persistent_buffer + current_buffer
            output_file.append(persistent_buffer)
            current_line_number = current_line_number + basic_defs.increment
            logging.debug(persistent_buffer)
            persistent_buffer, persistent_line_length = start_new_line(current_line_number)
        # when lines do need to be combined
        else:
            combined_line_length = persistent_line_length + len(basic_defs.statement_joining_character) + current_buffer_length
            logging.debug('Combined line length: %s', combined_line_length)
            need_new_line = check_new_line(tokenized_line)
            # when a new line is mandatory
            if need_new_line:
                if basic_type in ['bbc', 'riscos'] and current_buffer.startswith('DATA'):
                    # this is to avoid Out of DATA errors in BBC BASIC - it's the same code as the code below, I know, but using seperate functions for this stuff is trickier than it looks, and there's other features for this that are worth working on first
                    persistent_buffer = persistent_buffer.rstrip(basic_defs.statement_joining_character)
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug(persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug(persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                elif combined_line_length <= basic_defs.basic_line_length:
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug(persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                elif combined_line_length > basic_defs.basic_line_length:
                    persistent_buffer = persistent_buffer.rstrip(basic_defs.statement_joining_character)
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug(persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug(persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                continue
            # when a new line is not mandatory
            if combined_line_length <= basic_defs.basic_line_length:
                current_buffer = current_buffer + basic_defs.statement_joining_character
                persistent_buffer = persistent_buffer + current_buffer
                persistent_line_length = len(persistent_buffer)
            elif combined_line_length > basic_defs.basic_line_length:
                persistent_buffer = persistent_buffer.rstrip(basic_defs.statement_joining_character)
                output_file.append(persistent_buffer)
                current_line_number = current_line_number + basic_defs.increment
                logging.debug(persistent_buffer)
                persistent_buffer, persistent_line_length = start_new_line(current_line_number)
                persistent_buffer = persistent_buffer + current_buffer + basic_defs.statement_joining_character
                persistent_line_length = len(persistent_buffer)
    return output_file

def populate_label_data(working_file):
    """ This function populates a dictionary with labels and determines how many bytes to assume when replacing a line label. """
    file_length = len(working_file)
    line_count = 0
    label_dict = dict()
    # add labels to dictionary
    for line in working_file:
        if line.startswith('`'):
            label_dict[line] = 0
            line_count += 1
            logging.debug(line)
    lines_total = file_length - line_count
    logging.debug('Total number of lines: %s', lines_total)
    # determine how many bytes are needed when replacing labels
    if lines_total < 10:
        line_replacement = 1
    elif lines_total < 100:
        line_replacement = 2
    elif lines_total < 1000:
        line_replacement = 3
    elif lines_total < 10000:
        line_replacement = 4
    else:
        line_replacement = 5
    logging.debug('Line replacement value: %s', line_replacement)
    return label_dict, line_replacement

def remove_comments(commented):
    """ This will remove comments from the file. """
    # strip whitespace
    stripped = [line.strip() for line in commented]
    # strip comments
    uncommented = [a.rstrip(':') for a in [b.rstrip() for b in [re.sub(RE_QUOTES + r"'.*?$", '', c) for c in stripped]]]
    uncommented = list(filter(None, uncommented))
    return uncommented

# logger setup
logging.basicConfig(filename='bw.log', filemode='w', level=logging.DEBUG)

# set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('basic_type', choices=[b for b in [a for a in dir(basdefs) if not a.startswith('_')] if not b == 'prototype_def'], metavar='BASIC_Type', help='Specify the BASIC dialect to use')
parser.add_argument('input_filename', metavar='filename', help='Specify the file to process')
parser.add_argument('-p', '--paste-mode', dest='p', action='store_true', default=False, help='Sets paste to clipboard mode')
parser.add_argument('-l', '--line-length', dest='l', type=int, help='Set a non-default maximum BASIC line length')
parser.add_argument('-n', '--numbering_start', dest='n', type=int, help='Set the line number to begin numbering with')
parser.add_argument('-i', '--increment', dest='i', type=int, help='Set the increment between BASIC lines')
parser.add_argument('-o', '--output-filename', dest='o', help='Set the output filename')
args = parser.parse_args()

# get command line arguments
basic_type = args.basic_type
input_filename = args.input_filename

# other arguments - hard-coded for now
paste_format = args.p
basic_line_length = args.l
numbering = args.n
increment = args.i
user_filename = args.o

# auto-set paste format when needed
if basic_type.startswith('alt') or basic_type == 'trs80l1':
    paste_format = True
elif basic_type in ALWAYS_FILE_FORMAT or basic_type.startswith('zx'):
    paste_format = False

# open the input file
with open(input_filename) as file:
    original_file = file.readlines()

# set BASIC definition namedtuple
set_basic_type = getattr(basdefs, basic_type)
BasicDefs = namedtuple('BasicDefs', ['basic_line_length', 'combine', 'crunch', 'print_as_question', 'statement_joining_character', 'numbering', 'case', 'increment', 'abbreviate', 'tokenize', 'data_length'])
basic_defs = BasicDefs(*set_basic_type(paste_format, basic_line_length, numbering, increment))
logging.debug(basic_defs)

# remove comments
working_file = remove_comments(original_file)

# reformat DATA statements if needed
for index, line in enumerate(working_file):
    if line.startswith('#data'):
        working_file = reformat_data_statements(working_file, basic_defs)

# create a dictionary containing all the jump target labels
label_dict, line_replacement = populate_label_data(working_file)

# ZX Spectrum laziness feature - replace GOTO and GOSUB with GO TO and GO SUB
if basic_type == 'zxspectrum':
    for index, line in enumerate(working_file):
        working_file[index] = re.sub('GOTO' + RE_QUOTES, 'GO TO', line)
    for index, line in enumerate(working_file):
        working_file[index] = re.sub('GOSUB' + RE_QUOTES, 'GO SUB', line)

# abbreviate statements if needed
if basic_defs.abbreviate:
    script_dir = Path(__file__).resolve().parent
    rel_path = (basic_type + '.abv')
    abbrev_path = Path.joinpath(script_dir, rel_path)
    with open(abbrev_path) as abbrev_file:
        abbrev_dict = json.load(abbrev_file)
    for key in sorted(abbrev_dict, key=len, reverse=True):
        for index, line in enumerate(working_file):
            working_file[index] = re.sub(key + RE_QUOTES, abbrev_dict[key], line)

# renumber the BASIC file
working_file = renumber_basic_file(working_file, basic_defs, label_dict, line_replacement, basic_type)
logging.debug(label_dict)

# replace labels with line numbers
for key in sorted(label_dict, key=len, reverse=True):
    for index, line in enumerate(working_file):
        working_file[index] = re.sub(key + RE_QUOTES, str(label_dict[key]), line)

# warn if line is too long
for index, line in enumerate(working_file):
    if len(line) > basic_defs.basic_line_length:
        line_number_match = re.search(r'^\d*', line)
        line_number = line[line_number_match.span()[0]:line_number_match.span()[1]]
        logging.warning('Line number %s may be too long.', line_number)

# add space in between line number and rest of line for certain basic versions
if basic_type in ['bascom', 'amiga'] or basic_type.startswith('zx'):
    for index, line in enumerate(working_file):
        space_index = re.search(r'^\d*', line)
        working_file[index] = line[0:space_index.span()[1]] + ' ' + line[space_index.span()[1]:]

# add newlines back in to the file
atascii_file = None
if basic_type == 'atari' and not paste_format:
    atascii_list = [a.encode() for a in working_file]
    atascii_file = b'\x9b'.join(atascii_list)
    atascii_file = atascii_file + b'\x9b'
else:
    final_file = '\n'.join(working_file)
    final_file = final_file + '\n'

# add a POKE statement to Atari pasted files to expand the display so more text can be pasted in
if basic_type == 'atari' and paste_format:
    final_file = 'POKE 82,0\n' + final_file

# adjust case if needed when pasting
if basic_type in CBM_BASIC:
    final_file = final_file.lower()
elif paste_format and basic_defs.case == 'lower':
    final_file = final_file.lower()
elif paste_format and basic_defs.case == 'invert':
    final_file = final_file.swapcase()

# set the final filename
if user_filename:
    temp_filename = user_filename
else:
    temp_filename = input_filename
if basic_type == 'zx81':
    output_filename = temp_filename[0:-4] + '-out.b81'
elif basic_type == 'zxspectrum':
    output_filename = temp_filename[0:-4] + '-out.b82'
elif basic_type == 'amiga':
    output_filename = temp_filename[0:-4] + '.b'
elif basic_type == 'riscos':
    output_filename = temp_filename[0:-4] + ',ffb'
elif not user_filename:
    output_filename = temp_filename[0:-4] + '-out.bas'
else:
    output_filename = temp_filename

# change the newline type if needed
newline_type = '\r\n'
if basic_type in ['amiga', 'riscos']:
    newline_type = '\n'

# write or paste the renumbered file
if paste_format:
    pyperclip.copy(final_file)
if not paste_format or user_filename:
    if atascii_file:
        with open(output_filename, 'wb') as file:
            file.write(atascii_file)
    else:
        with open(output_filename, 'w', newline=newline_type) as file:
            file.write(final_file)

# output to console that the file has been saved
if not paste_format or user_filename:
    print(input_filename + ' has been saved as ' + output_filename)

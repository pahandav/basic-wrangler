#!/usr/bin/env python3
""" basic-wrangler - A BASIC program listing line renumberer/cruncher. """

import argparse
import json
import logging
import re
import sys
import duallog
from collections import namedtuple
from pathlib import Path

import pyperclip
from gooey import Gooey, GooeyParser

import common.functions as functions
import convert.helpers as helpers
import defs.basdefs as basdefs
import renum.renumber as renumber
import convert.label as label
from lex.genlex import generate_splitter
# constants
from common.constants import RE_QUOTES

if len(sys.argv) >= 2:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')

ALWAYS_FILE_FORMAT = ['bascom', 'amiga', 'riscos', 'gwbasic']
CBM_BASIC = ['pet', 'vic20', 'c64', 'plus4', 'c128']

def renum(args):
    """ Renumbers BASIC listings. """
    # set variables from CLI or GUI arguments
    basic_type = args.basic_type
    input_filename = args.input_filename
    paste_format = args.paste_mode
    basic_line_length = args.line_length
    numbering = args.numbering
    increment = args.increment
    user_filename = args.output_filename


    # open the input file
    with open(input_filename) as file:
        original_file = file.read()
    split_file = original_file.splitlines()

    # get BASIC definition namedtuple
    basic_defs, paste_format = basdefs.set_basic_defs(basic_type, paste_format, basic_line_length, numbering, increment)

    # strip and remove comments
    working_file = functions.strip_file(split_file)
    working_file = functions.remove_comments(working_file)

    # reformat DATA statements if needed
    for line in working_file:
        if line.startswith('#data'):
            working_file = functions.reformat_data_statements(working_file, basic_defs)

    # create a dictionary containing all the jump target labels
    label_dict, line_replacement = renumber.populate_label_data(working_file)

    # ZX Spectrum laziness feature - replace GOTO and GOSUB with GO TO and GO SUB
    if basic_type == 'zxspectrum':
        for index, line in enumerate(working_file):
            working_file[index] = re.sub('GOTO' + RE_QUOTES, 'GO TO', line)
        for index, line in enumerate(working_file):
            working_file[index] = re.sub('GOSUB' + RE_QUOTES, 'GO SUB', line)

    # abbreviate statements if needed
    if basic_defs.abbreviate:
        working_file = basdefs.abbreviate(working_file, basic_type)

    # renumber the BASIC file
    working_file = renumber.renumber_basic_file(working_file, basic_defs, label_dict, line_replacement, basic_type)
    logging.debug(label_dict)

    # replace labels with line numbers
    for key in sorted(label_dict, key=len, reverse=True):
        for index, line in enumerate(working_file):
            working_file[index] = re.sub(key + RE_QUOTES, str(label_dict[key]), line)

    # add newlines back in to the file
    atascii_file = None
    if basic_type == 'atari' and not paste_format: # special ATASCII routine
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

def convert(args):
    """ Converts between listing formats. """
    input_filename = args.input_filename
    user_filename = args.output_filename
    with open(input_filename) as file:
        original_file = file.read()
    split_file = original_file.splitlines()
    working_file = functions.strip_file(split_file)
    if args.split:
        split_string = generate_splitter()
        new_file = list()
        for line in working_file:
            temp1 = re.split('(' + split_string + r'|\".*?\")', line)
            temp2 = [x for x in temp1 if x.strip()]
            new_line = ' '.join(temp2)
            new_file.append(new_line)
        working_file = new_file
    if args.label:
        working_file = label.label_listing(working_file)
    if args.c64_list:
        working_file = helpers.c64_list(working_file)
    if args.data_formatter:
        working_file = helpers.data_format(working_file)
    final_file = '\n'.join(working_file)
    final_file = final_file + '\n'
    if user_filename:
        temp_filename = user_filename
    else:
        temp_filename = input_filename
    if not user_filename:
        output_filename = temp_filename[0:-4] + '-out.bas'
    else:
        output_filename = temp_filename
    with open(output_filename, 'w') as file:
        file.write(final_file)
    print(input_filename + ' has been saved as ' + output_filename)


@Gooey(program_name='BASIC Wrangler', default_size=(610, 675), navigation='TABBED')
def main():
    """ The main function. """
    duallog.setup('logs')
    # logger setup
    #logging.basicConfig(filename='bw.log', filemode='w', level=logging.DEBUG)

    # set up argument parser and get arguments
    parser = GooeyParser(description="A BASIC program listing line renumberer/cruncher.")
    subparsers = parser.add_subparsers(help='sub-command help')
    # renumber subparser
    parser_renum = subparsers.add_parser('renum', help='renum help')
    parser_renum.add_argument('basic_type', choices=basdefs.get_basic_dialects(), metavar='BASIC_Type', help='Specify the BASIC dialect to use')
    parser_renum.add_argument('input_filename', metavar='filename', help='Specify the file to process', widget='FileChooser')
    parser_renum.add_argument('-o', '--output-filename', dest='output_filename', help='Set the output filename', widget='FileSaver')
    parser_renum.add_argument('-p', '--paste-mode', dest='paste_mode', action='store_true', default=False, help='Sets paste to clipboard mode')
    parser_renum.add_argument('-l', '--line-length', dest='line_length', type=int, help='Set a non-default maximum BASIC line length')
    parser_renum.add_argument('-n', '--numbering_start', dest='numbering', type=int, help='Set the line number to begin numbering with')
    parser_renum.add_argument('-i', '--increment', dest='increment', type=int, help='Set the increment between BASIC lines')
    parser_renum.set_defaults(func=renum)
    # convert subparser
    # TODO: Add a mutually exclusive group here.
    parser_convert = subparsers.add_parser('convert', help='convert help')
    parser_convert.add_argument('input_filename', metavar='filename', help='Specify the file to process', widget='FileChooser')
    parser_convert.add_argument('-l', '--label', action='store_true', default=False, help='Convert from numbered listing')
    parser_convert.add_argument('-c', '--c64-list', action='store_true', default=False, help='Convert from C64List format')
    parser_convert.add_argument('-d', '--data-formatter', action='store_true', default=False, help='Reformat DATA Statments')
    parser_convert.add_argument('-s', '--split', action='store_true', default=False, help='Split a crunched listing')
    parser_convert.add_argument('-o', '--output-filename', dest='output_filename', help='Set the output filename', widget='FileSaver')
    parser_convert.set_defaults(func=convert)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()

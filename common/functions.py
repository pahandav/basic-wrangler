""" This module contains functions that are accessed from multiple other modules. """
import logging
import re

from common.constants import RE_QUOTES


def remove_comments(commented):
    """ This will remove comments from the file. """
    # strip whitespace
    stripped = [line.strip() for line in commented]
    # strip comments
    uncommented = [a.rstrip(':') for a in [b.rstrip() for b in [re.sub(RE_QUOTES + r"'.*?$", '', c) for c in stripped]]]
    uncommented = list(filter(None, uncommented))
    return uncommented

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
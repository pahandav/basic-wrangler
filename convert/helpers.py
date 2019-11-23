""" This contains former helper scripts. """
import re
import sys

RE_QUOTES = r'(?=([^"]*"[^"]*")*[^"]*$)'

def c64_list(input_file):
    """ This converts from C64List format. """
    for index, _ in enumerate(input_file):
        if input_file[index].startswith('{:') and input_file[index].endswith('}'):
            input_file[index] = input_file[index].replace('{:', '_')
            input_file[index] = input_file[index].replace('}', ':')
        else:
            input_file[index] = input_file[index].replace('{:', '_')
            input_file[index] = input_file[index].replace('}', '')
        # This replaces every REM not in quotes with an apostrophe
        input_file[index] = re.sub('REM' + RE_QUOTES, '\'', input_file[index])
    return input_file

def data_format(input_file):
    """ This reformats DATA statements. """
    data_statement = '#data\n'
    for index, line in enumerate(input_file):
        if line.startswith('DATA'):
            stripped = line.lstrip('DATA')
            # This replaces every comma in between data statement values not in quotes with a newline
            temp = stripped + '\n'
            temp = re.sub(',' + RE_QUOTES, '\n', temp)
            temp = temp.lstrip()
            data_statement = data_statement + temp
            input_file[index] = ''
    data_statement = data_statement + '#enddata'
    final = list(filter(None, input_file))
    final.append(data_statement)
    return final

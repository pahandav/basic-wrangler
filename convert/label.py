""" This script contains the routines to convert a numbered listing to a labelled listing. """

from lex.genlex import generate_label_lexer
import sys
import logging

def tokenize_line(Lexer, untokenized_line):
    """ This function returns a tokenized line as a list. """
    Lexer.input(untokenized_line)
    token_list = list()
    try:
        for tok in Lexer.tokens():
            logging.debug(tok)
            token_list.append(tok)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
    return token_list

def sanity_check_listing(Lexer, numbered_file):
    """ First pass - This function returns a list of all the line numbers in the file. """
    original_line_numbers = list()
    for line in numbered_file:
        tokenized_line = tokenize_line(Lexer, line)
        if tokenized_line[0].type == 'LINE':
            if len(original_line_numbers) == 0:
                original_line_numbers.append(tokenized_line[0].val)
            else:
                if tokenized_line[0].val in original_line_numbers:
                    # Duplicate Line sanity check
                    logging.critical('Fatal Error! Line number ' + tokenized_line[0].val + ' is a duplicate!')
                    sys.exit(1)
                if int(tokenized_line[0].val) < int(original_line_numbers[-1]):
                    # Out of order check.
                    logging.warning('Line number ' + tokenized_line[0].val + ' is out of order.')
                original_line_numbers.append(tokenized_line[0].val)
    return original_line_numbers

def extract_jump_targets(Lexer, numbered_file, original_line_numbers):
    """ Second pass - This function returns a set of jump targets. """
    jump_targets = set()
    for line in numbered_file:
        tokenized_line = tokenize_line(Lexer, line)
        tokenized_line_length = len(tokenized_line)
        indices = [i for i, x in enumerate(tokenized_line) if x.type == "FLOW"]
        logging.debug(line)
        logging.debug(indices)
        for index in indices:
            if index+1 < tokenized_line_length:
                if tokenized_line[index+1].type == 'NUMBER':
                    target = tokenized_line[index+1].val
                    logging.debug(target)
                    if target not in original_line_numbers:
                        logging.critical('Fatal Error! Attempt to jump to line number ' + target + ' is invalid!')
                        sys.exit(1)
                    jump_targets.add(target)
    logging.debug(jump_targets)
    return jump_targets

def label_listing(numbered_file):
    """ This function returns a labeled BASIC listing. """
    basic_type = 'generic'
    Lexer = generate_label_lexer(basic_type)
    original_line_numbers = sanity_check_listing(Lexer, numbered_file)
    jump_targets = extract_jump_targets(Lexer, numbered_file, original_line_numbers)
    sys.exit()

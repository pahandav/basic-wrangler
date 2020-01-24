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

def label_listing(numbered_file):
    """ This function returns a labeled BASIC listing. """
    basic_type = 'generic'
    Lexer = generate_label_lexer(basic_type)
    for line in numbered_file:
        tokenized_line = tokenize_line(Lexer, line)
        for token in tokenized_line:
            print(token.type)
            print(token.val)
    sys.exit()

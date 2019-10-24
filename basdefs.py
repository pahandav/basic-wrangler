""" This module contains BASIC dialect definitions for basicwrangler.

    TODO: Replace this entire module of functions with YAML or JSON definitions. """

def prototype_def(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ A prototypical BASIC definition.

    Modify according to the parameters of the desired version of BASIC. """

    if basic_line_length is None and paste_format: basic_line_length = 72 # set maximum basic line length for paste mode
    elif basic_line_length is None: basic_line_length = 128 # set maximum basic line length for file mode
    combine = True # decide whether to combine lines or not
    crunch = 0 # set the crunching level - 1 has no spaces, 0 has spaces - numbers above 1 reserved for future use
    print_as_question = False # this decides whether to abbreviate PRINT as ?
    statement_joining_character = ':' # this is the character that joins statements together - almost always ':'
    if numbering is None: numbering = 0 # this is the line number to start numbering with
    case = '' # determines whether to change case on output - should usually be blank
    if increment is None: increment = 1 # this is the line numbering increment
    abbreviate = False # this is to indicate the use of an abbreviation dictionary - should normally be False
    tokenize = False # this is to indicate the use of a tokenizer
    # data_length = 96 # this is for when a different data statement length is needed
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def alt4k(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Altair 8800 4K BASIC. """
    if basic_line_length is None: basic_line_length = 72
    combine = True
    crunch = 1
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def alt8k(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Altair 8800 8K BASIC. """
    if basic_line_length is None: basic_line_length = 72
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def altext(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Altair 8800 Extended BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def altdisk(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Altair 8800 Disk BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def cpm4(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ CP/M BASIC-80 version 4. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def cpm5(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ CP/M BASIC-80 version 5. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def bascom(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Microsoft BASCOM. """
    if basic_line_length is None: basic_line_length = 252
    combine = False
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 1
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def pet(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore PET BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 79
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def apple2(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Applesoft BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 239
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def trs80l1(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ TRS-80 Level 1 BASIC. """
    if basic_line_length is None: basic_line_length = 70
    combine = True
    crunch = 1
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 1
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = True
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def trs80l2(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ TRS-80 Level 2 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 241
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'invert'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def trs80m4(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ TRS-80 Model 4 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 241
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def atari(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Atari 8-bit BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 119
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = True
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def ti99(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ TI 99/4A BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 140
    elif basic_line_length is None: basic_line_length = 128
    combine = False
    crunch = 0
    print_as_question = False
    statement_joining_character = '::'
    if numbering is None: numbering = 1
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    data_length = 96
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def ti99xb(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ TI 99/4A Extended BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 140
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = False
    statement_joining_character = '::'
    if numbering is None: numbering = 1
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    data_length = 96
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def vic20(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore VIC-20 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 87
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def coco(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Tandy Color BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def coco3(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Tandy CoCo 3 BASIC.

    Note: This is a temporary definition, it will probably be deleted at some point. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def apple3(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Apple /// Business BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def c64(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore 64 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 80
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def plus4(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore PLUS/4 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 80
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def c128(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore 128 BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 80
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = 'lower'
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def zx81(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Sinclair ZX-81 BASIC. """
    basic_line_length = 65535
    combine = False
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def zxspectrum(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Sinclair ZX Spectrum BASIC. """
    basic_line_length = 65535
    combine = True
    crunch = 0
    print_as_question = False
    statement_joining_character = ' : '
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def bbc(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ BBC Micro BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 239
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def oric(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Tangerine Oric BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 78
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def msx(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ MSX BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 239
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 1
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def adam(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Coleco ADAM SmartBASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 100
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def cpc(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Amstrad CPC BASIC. """
    if basic_line_length is None and paste_format: basic_line_length = 186
    elif basic_line_length is None: basic_line_length = 128
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 1
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def amiga(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Commodore Amiga ACE BASIC Compiler. """
    if basic_line_length is None: basic_line_length = 252
    combine = False
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 1
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def riscos(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ BBC RISC OS BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = False
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

def gwbasic(paste_format, basic_line_length, numbering, increment, data_length=None):
    """ Microsoft GW-BASIC. """
    if basic_line_length is None: basic_line_length = 252
    combine = True
    crunch = 0
    print_as_question = True
    statement_joining_character = ':'
    if numbering is None: numbering = 0
    case = ''
    if increment is None: increment = 1
    abbreviate = False
    tokenize = False
    return (basic_line_length, combine, crunch, print_as_question, statement_joining_character, numbering, case, increment, abbreviate, tokenize, data_length)

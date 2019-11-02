""" This module contains the abbreviation routines. """
import json
import re
from pathlib import Path

from common.constants import RE_QUOTES


def abbreviate(working_file, basic_type):
    """ Returns the file with keywords abbreviated. """
    script_dir = Path(__file__).resolve().parent
    rel_path = (basic_type + '.abv')
    abbrev_path = Path.joinpath(script_dir, rel_path)
    with open(abbrev_path) as abbrev_file:
        abbrev_dict = json.load(abbrev_file)
    for key in sorted(abbrev_dict, key=len, reverse=True):
        for index, line in enumerate(working_file):
            working_file[index] = re.sub(key + RE_QUOTES, abbrev_dict[key], line)
    return working_file

#!/usr/bin/env python3
""" CLI Entry point. """

import sys
if len(sys.argv) <= 2:
    sys.argv.append('-h')
sys.argv.append('--ignore-gooey')
import basicwrangler

basicwrangler.main()

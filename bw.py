#!/usr/bin/env python3
""" Entry point. """

import sys
if len(sys.argv) >= 2:
    sys.argv.append('--ignore-gooey')
import basicwrangler

basicwrangler.main()

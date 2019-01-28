#!/usr/bin/env python3
"""
usage: polypy [ -v ... ] [options] sip config [<column_definitions>...]
       polypy [ -v ... ] [options] sip generate <extension> from <file> [<args>...]

sip commands:

  config         Create a configuration file that is used to read your CSV data source.
  generate       Generate one or more sip.conf device definitions from your CSV data source.

options:
  -v             Be verbose
  -f, --force    Force the setting.

"""

from pprint import pprint
from docopt import docopt
import sys
import os
import json
from poly_py_tools.sip_parser import SipConfParser
from poly_py_tools.pw_strength_calculator import PasswordStrengthCalculator

args = docopt(__doc__)

pprint(args)
config_dir = "/etc/polypy/"
config_path = os.path.join(config_dir, "polypy.conf")
configs = None

if args['config']:
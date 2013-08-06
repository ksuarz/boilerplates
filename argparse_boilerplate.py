#!/usr/bin/env python
'''

'''

import argparse
import sys


if __name__ == '__main__':
    # Set up command line options
    parser = argparse.ArgumentParser(
            prog='$PROGRAM.py',
            description='$PROGRAM - $DESCRIPTION.',
            epilog='')
    parser.add_argument(
            'positional-argument',
            help='')
    parser.add_argument(
            '-b',
            '--boolean-option',
            action='store_true',
            help='')
    parser.add_argument(
            '-i',
            '--integer-option',
            metavar='INT',
            default=0,
            dest='var_name_to_store_in',
            type=int,
            help='')
    parser.add_argument(
            '--long-option',
            metavar='OPTION',
            default='',
            help='')
    parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-a', action='store_true')
    group.add_argument('-b', action='store_false')

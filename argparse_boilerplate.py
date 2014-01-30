import argparse


if __name__ == '__main__':
    # Set up command line options
    parser = argparse.ArgumentParser(
            prog='',
            description='',
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

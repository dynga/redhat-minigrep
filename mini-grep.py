#!/usr/bin/env python

import argparse
import re as regex
import fileinput
import sys
  

def search(file_paths, pattern, line_nums):
    result = []
    try: 
        with fileinput.input(files=file_paths) as text:
            for line in text:
                if regex.search(pattern, line):
                    if not line_nums:
                        result.append(line.strip())
                    else:
                        result.append(''.join([
                                            str(text.filelineno()), 
                                            " ", 
                                            line.strip()]))
            if not result:
                result.append('No occurencce of PATTERN found in file.')
            return result
    except FileNotFoundError as error:
        result.append('Error: File not found')
        return result
    

def compile_regex(pattern):
    try:
        return regex.compile(pattern)
    except regex.error as error:
        return None


if __name__ == '__main__':

    argparser = argparse.ArgumentParser(
        prog='mini-grep',
        description='Simple implementation of the grep utility. \
            Goes through every argument in FILE and prints the whole line \
            in which PATTERN is found. If no arguments are passed to FILE,\
            it will parse entries from the standard input. By default, it\
            also outputs the line number of each printed line.'
    )

    argparser.add_argument(
        '-q', 
        action='store_false', 
        help='If this option is given, mini-grep will only output lines, \
            omitting the matching line numbers.')
    argparser.add_argument(
        '-e', 
        metavar='PATTERN', 
        required=True, 
        help='Pattern to scan files for. Has to be a valid \
            regular expression. Required argument.')
    argparser.add_argument(
        'FILE', 
        nargs='*', 
        default=[], 
        help='Zero or more files to scan for the pattern given with -e. \
            If number of files is zero, standard input will be scanned.')

    args = argparser.parse_args()
    
    pattern = compile_regex(args.e)
    
    if not pattern:
        print('Regular expression error')
        sys.exit(1)

    files = args.FILE
    include_line_numbers = args.q

    [print(item) for item in search(files, pattern, include_line_numbers)]

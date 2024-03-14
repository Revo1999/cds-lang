'''
This file contains useful funtions for working with python

Will get updated throughout the semester

Author: Victor Rasmussen
'''

import os


def work_here():
    absolute_path = os.path.abspath(__file__)
    directory_name = os.path.dirname(absolute_path)
    os.chdir(directory_name)


class colorbank:
    default = '\033[0m'
    hackergreen = '\x1b[38;5;118m'
    white = '\x1b[37m'
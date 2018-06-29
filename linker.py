# Title: AAMPS_linker
# Author: Joseph Whittington
# Dependencies: python 2.7.*
# Description: This script links the directory it's in to AMPPS

# **run the program by typing "python make_json.py with optional filepath"

import os
from sys import argv

def main(argv):
    ampps_path = argv[1] if len(argv) > 1 else '/Applications/AMPPS/www'
    try:
        os.symlink(os.getcwd(), os.path.join(ampps_path ,os.path.basename(os.getcwd())))
    except: 
        print('\nYour AMPPS root folder is not in the default location(/Applications/AMPPS/www)')
        print('To use linker specify the path to current aamps root folder after the file name')
        print('Ex: "python linker.py <ampps_path>"\n')

if __name__ == '__main__':
    main(argv)
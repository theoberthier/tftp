#!/usr/bin/env python3
"""
TFTP Server Command.
"""

########################################################################
#                               Authors                                #
#                  Théo Morin : contact@theomorin.fr                   #
#           Théo Berthier : theo.berthier@etu.u-bordeaux.fr            #
########################################################################


import sys
import os
import argparse
import tftp

TIMEOUT = 2
PORT = 6969

parser = argparse.ArgumentParser(prog='tftp-server')
parser.add_argument('-p', '--port', type=int, default=PORT)
parser.add_argument('-t', '--timeout', type=int, default=TIMEOUT)
parser.add_argument('-c', '--cwd',  type=str, default='')
parser.add_argument('--thread', action='store_true')
args = parser.parse_args()

# change current working directory
if args.cwd != '':
    try:
        os.chdir(args.cwd)
    except:
        print("\033[91mLe dossier n'existe pas.")
        sys.exit(1)

# run main server loop
tftp.runServer(('', args.port), args.timeout, args.thread)

# EOF

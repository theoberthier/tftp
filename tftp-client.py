#!/usr/bin/env python3
"""
TFTP Client Command.
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
BLKSIZE = 512

parser = argparse.ArgumentParser(prog='tftp-client')
parser.add_argument('-p', '--port', type=int, default=PORT)
parser.add_argument('-t', '--timeout', type=int, default=TIMEOUT)
parser.add_argument('-b', '--blksize', type=int, default=BLKSIZE)
parser.add_argument('-c', '--cwd',  type=str, default='')
parser.add_argument('cmd', type=str, choices=['get', 'put'])
parser.add_argument('host', type=str)
parser.add_argument('filename', type=str)
parser.add_argument('targetname', type=str, nargs='?', default='')
args = parser.parse_args()

# change target filename
if args.targetname == '': args.targetname = args.filename

# change current working directory
if args.cwd != '':
    try:
        os.chdir(args.cwd)
    except:
        print("\033[93mLe dossier n'existe pas.")
        sys.exit(1)

# get request
if(args.cmd == 'get'):
    tftp.get((args.host, args.port), args.filename, args.targetname, args.blksize, args.timeout)
    # je ferai bien une boucle qui attend les données et quand on reçois un paquet on renvoie ack
    # et on écrit dans notre fichier côté client

# put request
if(args.cmd == 'put'):
    tftp.put((args.host, args.port), args.filename, args.targetname, args.blksize, args.timeout)
    # ici je pense qu'un file traitement peux être utiliser ? pour lire le fichier et l'envoyer en requête, 
    # côté serveur on traitera des DAT donc dans la condition opcode == 3 on récupère le dat dans un string,
    # et quand le string contient tout le message on utilise write pour écrire dans le fichier voulu   

# EOF
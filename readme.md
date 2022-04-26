# Projet TFTP en Python

### Authors
- Théo Morin (contact@theomorin.fr)
- Théo Berthier (theo.berthier@etu.u-bordeaux.fr)


### Describe
Création d'un serveur et d'un client d'une version allégée du protocol FTP (TFTP).

### Server params
- L'option -h affiche l'aide sur la commande.  
- L'option -p PORT indique le numéro de port du serveur (par défaut, 6969).  
- L'option -t TIMEOUT indique le délai en secondes à partir duquel on considère que l'envoi ou la réception échoue (par défaut, 2).  
- L'option -c CWD permet de changer le répertoire courant dans lequel les fichiers (avec des chemins relatifs) sont lus ou écrits.  
- L'option --thread (côté serveur uniquement) indique au serveur de traiter des requêtes clientes en parallèle, en déléguant chaque transfert de fichier à un thread particulier côté serveur (par défaut, False). 

### Client params
- L'option -h affiche l'aide sur la commande.  
- L'option -p PORT indique le numéro de port du serveur (par défaut, 6969).  
- L'option -t TIMEOUT indique le délai en secondes à partir duquel on considère que l'envoi ou la réception échoue (par défaut, 2).  
- L'option -c CWD permet de changer le répertoire courant dans lequel les fichiers (avec des chemins relatifs) sont lus ou écrits.  
- L'option -b BLKSIZE (côté client uniquement) indique la taille en octet du bloc de données utilisée pour transférer les fichiers (par défaut, 512).  

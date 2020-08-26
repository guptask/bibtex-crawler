#!/usr/bin/env python3

import glob
#from pprint import pprint
from bibtexparser.bparser import BibTexParser
import sys, getopt, logging

logging.basicConfig(filename='error.log', level=logging.DEBUG, 
        format='%(asctime)s %(levelname)s %(message)s')
logger=logging.getLogger(__name__)


def main(argv):
    rootpath = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except:
        print("parse.py -p <rootpath>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("parse.py -p <rootpath>")
            sys.exit()
        elif opt in ("-p", "--path"):
            rootpath = arg
        else:
            print("Invalid option. Use parse.py -p <rootpath>")
            sys.exit()

    files = glob.glob(rootpath + '/**/*.bib', recursive=True)
    for counter, entry in enumerate(files):
        print('{0}: Parse {1}'.format(counter, entry))
        parser = BibTexParser()
        with open(entry, encoding='utf-8') as bibtex_file:
            try:
                logger.info('Parsing %s', entry)
                bib_database = parser.parse_file(bibtex_file)
            except:
                logger.error(sys.exc_info()[0])


if __name__ == "__main__":
    main(sys.argv[1:])

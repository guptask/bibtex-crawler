#!/usr/bin/env python3

import glob
from pprint import pprint
from bibtexparser.bparser import BibTexParser
#from pybtex.database.input import bibtex
import sys, getopt

def customizations(record):
    """Use some functions delivered by the library
            :param record: a record
            :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record

def main(argv):
    rootpath = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
        print("parse.py -p <rootpath>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("parse.py -p <rootpath>")
            sys.exit()
        elif opt in ("-p", "--path"):
            rootpath = arg

    files = glob.glob(rootpath + '/**/*.bib', recursive=True)
    for counter, entry in enumerate(files):
        print('{0}: Parse {1}'.format(counter, entry))
        parser = BibTexParser()
        #parser.customization = customizations
        with open(entry, encoding='utf-8') as bibtex_file:
            try:
                bib_database = parser.parse_file(bibtex_file)
                #print(bib_database.entries)
                #parser = bibtex.Parser()
                #bib_data = parser.parse_file(bibtex_file)
                #bib_data.entries.keys()
                #break
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")


if __name__ == "__main__":
    main(sys.argv[1:])

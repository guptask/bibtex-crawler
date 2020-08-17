#!/usr/bin/env python3

import glob
from pprint import pprint
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
#from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode

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

files = glob.glob("papers" + '/**/*.bib', recursive=True)
for bibfile in files:
    with open(bibfile, encoding='utf-8') as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        #parser.customization = homogenize_latex_encoding
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        print(bib_database.entries)

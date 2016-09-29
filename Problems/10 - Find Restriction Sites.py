__author__ = 'paulsalvatore57'

from Rosalind.SEQUENCE import *

sequences = FASTA_LOAD('test1')

for i in sequences:
    print i.getID()
    sites = i.findRestrictionSites()
    for j in sites:
        print j[0], j[1]






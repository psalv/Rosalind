__author__ = 'paulsalvatore57'

from Rosalind.SEQUENCE import *

def findHighestGC(file, toPrint = False):
    """Returns the sequence code with the highest GC content in the form: [ID, GC content]"""
    seqs = FASTA_LOAD(file)
    highest = None
    for seq in seqs:

        if highest == None:
            highest = [seq.getID(), seq.getGC()]

        elif seq.getGC() > highest[1]:
            highest = [seq.getID(), seq.getGC()]

    if toPrint:
        print highest[0][1:], '\n', highest[1] * 100

    return highest

findHighestGC('Q5 SEQUENCES', True)
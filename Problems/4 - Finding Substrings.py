__author__ = 'paulsalvatore57'

from Rosalind.SEQUENCE import *


def findMotifs(fileName, motif, toPrint = False):
    seq = RAW_LOAD(fileName)
    positions = []
    last = 0

    while len(seq) >= len(motif):
        try:
            pos = seq.index(motif) + 1
            positions.append(pos + last)
            last = pos + last
            seq = seq[pos:]
        except ValueError:
            break

    if toPrint:
        for pos in positions:
            print 'Motif at position:', pos, '-', pos + len(motif) - 1

    return positions



motifs = findMotifs('Q4 SEQUENCE', 'GTTGGGTGT')

def printCorrect(list):
    ans = ''
    for i in list:
        ans += str(i) + ' '
    print ans

printCorrect(motifs)

__author__ = 'paulsalvatore57'

from Rosalind.SEQUENCE import *


def genProfile(file):
    """Builds the consensus sequence from FASTA files, prints the sequence along with the prevalence of each base in each position.
    Note: has a bias of the form C < G < T < A meaning that given 5 of each in a position the sequence will show a A."""
    seqs = FASTA_LOAD(file)
    length = None
    dA = {}
    dT = {}
    dG = {}
    dC = {}
    for seq in seqs:
        s = seq.getSeq()

        if length == None:
            length = len(s)

        if dA == {}:
            for i in xrange(length):
                dA[i] = 0
                dT[i] = 0
                dG[i] = 0
                dC[i] = 0

        for pos in xrange(length):
            if s[pos] == 'A':
                dA[pos] += 1
            elif s[pos] == 'T':
                dT[pos] += 1
            elif s[pos] == 'G':
                dG[pos] += 1
            else:
                dC[pos] += 1

    consensus = ''

    for pos in xrange(length):
        most = dA[pos]
        letter = "A"
        if dT[pos] > most:
            most, letter = dT[pos], 'T'
        if dG[pos] > most:
            most, letter = dG[pos], 'G'
        if dC[pos] > most:
            most, letter = dC[pos], 'C'

        consensus += letter

    print consensus
    profileOutput(dA, dT, dG, dC)


def profileOutput(dA, dT, dG, dC):
    """Takes in four dictionaries each mapping a DNA positions to how many of each nucleotide is present in this position among all of the FASTA files.
    Prints this data in a legible manner."""
    length = max(dA)
    A = 'A: '
    C = 'C: '
    G = 'G: '
    T = 'T: '
    for i in xrange(length + 1):
        A += str(dA[i]) + ' '
        C += str(dC[i]) + ' '
        G += str(dG[i]) + ' '
        T += str(dT[i]) + ' '
    print A + '\n' + C + '\n' + G + '\n' + T

genProfile('test1')
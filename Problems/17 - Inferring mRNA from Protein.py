

from Rosalind.SEQUENCE import RAW_LOAD

def findmRNAPermutations(file):
    """Finds the number of possible permutations of mRNA that could generate the given protein sequence."""
    seq = RAW_LOAD(file)
    codons = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2,\
            'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2, 'STOP': 3}
    ways = 3
    for aa in seq:
        ways *= codons[aa]
        ways = ways % 10**6
    return ways

# print findmRNAPermutations('test1')
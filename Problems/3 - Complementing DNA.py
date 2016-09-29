__author__ = 'paulsalvatore57'


def givePair(nuc, RNA = False):
    if nuc == 'A':
        if RNA:
            return 'U'
        else:
            return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'U':
        return 'A'
    elif nuc == 'C':
        return 'G'
    else:
        return 'C'

def complement(file):
    file = open(file, 'r')
    ans = ''
    for line in file:
        length = len(line)
        spot = 1
        while spot <= length:
            ans += givePair(line[-spot])
            spot += 1
    return ans


complement('Q3 SEQUENCE')




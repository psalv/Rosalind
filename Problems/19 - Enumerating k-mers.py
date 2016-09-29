
import itertools


def enumerateThem(file):
    """Uses itertools to find and print all of the possible combinations of the given characters with a repeat of k (with replacement)."""
    file = open(file)
    letters = file.readline().split()
    k = int(file.readline())

    comb = itertools.product(letters, repeat = k)

    toPrint = ''
    for i in comb:
        for j in i:
            toPrint += j
        toPrint += '\n'
    print toPrint

enumerateThem('test1')
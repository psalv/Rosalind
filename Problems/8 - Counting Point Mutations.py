__author__ = 'paulsalvatore57'

def countPoints(file):
    """Counts point mutants between two equal length DNA strands"""
    file = open(file, 'r')
    original = None
    m = 0
    for line in file:
        if original == None:
            original = line.rstrip()
        else:
            mutant = line.rstrip()
    for n in xrange(len(original)):
        if original[n] != mutant[n]:
            m += 1
    print m



import math, itertools

def allPermutations(n):
    """Uses itertools to find and print all of the possible permutations of the factorial components of n."""
    print math.factorial(n)
    toIter = ''
    for i in xrange(1, n + 1):
        toIter += str(i)
    combinations = itertools.permutations(toIter)
    toPrint = ''
    for i in combinations:
        for j in i:
            toPrint += j + ' '
        toPrint += '\n'
    print toPrint

# allPermutations(5)





import itertools


def toString(i):
    st = ''
    for j in i:
        st += j
    return st

def enumerateThemAll(file):
    """Uses itertools to find and print all of the possible combinations of the given characters with a repeat of k or less(with replacement).
    Then sorts the list based on the order in which they appeared in the original input."""
    file = open(file)
    letters = file.readline().split()
    k = int(file.readline())

    combs = []

    for i in xrange(k, 0, -1):
        comb = itertools.product(letters, repeat = i)
        for j in comb:
            combs.append(toString(j))

    dictL = {}
    for i in xrange(len(letters)):
        dictL[letters[i]] = i

    sortedList = []
    for i in xrange(len(letters)):
        sortedList.append([])

    for i in combs:
        sortedList[dictL[i[0]]].append(i)

    toPrint = ''
    for l in sortedList:
        for i in l:
            for j in i:
                toPrint += j
            toPrint += '\n'
    print toPrint


#The above works but I think they want a more concise lexicographical organization.

#For instance to order D N A:
    #D
    #D D
    #D D D
    #D D N
    #D D A
    #D N
    #D N D
    #D N N
    #D N A
    #D A
    #D A D
    #D A N
    #D A A

#This type of pattern will repeat for N and A, and I think this is what the question wants.




def lexEnumerate(file):
    file = open(file)
    letters = file.readline().split()
    le = len(letters)
    k = int(file.readline())

    combs = []


    for i in xrange(1, k + 1):
        combs.append([])
        comb = itertools.product(letters, repeat=i)
        for j in comb:
            combs[-1].append(toString(j))

    inOrder = []

    for j in xrange(le):
        for i in xrange(k):
            inOrder.append(combs[i][:le**i])
            combs[i] = combs[i][le**i:]


    toPrint = ''
    for l in inOrder:
        for i in l:
            for j in i:
                toPrint += j
            toPrint += '\n'
    print toPrint


# lexEnumerate('test1')


#This still doesn't quite work but it's very close.
#I think the only way to answer this question sanely is to generate the combinations in a different manner.


__author__ = 'paulsalvatore57'



#I'm going to be given up to 100 1 kbp DNA sequences (FASTA) and want to fidn the longest shared motif.


#Now I can't conceivable check every length substring and see if it is in every other string, that would be horribly inefficient.
#One idea I'm having is to use sets and then the intersection tool, but that would still require me to break down each string to it's substring constituents.
#This seems excessive.

#I'm going to try and do this, however since I've realized I only need to break down one string to it's constituents.

#A SUFFIX TREE is what I found to be the actual way for handling large amounts of text, but it may not be necessary here.

import time
from Rosalind.SEQUENCE import *


start_time = time.time()

def sharedMotifs(file):
    seqs = FASTA_LOAD(file)
    temp = seqs[0].getSeq()

    allSubStr = set()
    allSubStr.add(temp)

    for i in xrange(1, len(temp)):
        for j in xrange(1, len(temp)):

            if i + j > len(temp):
                break

            allSubStr.add(temp[i:i+j])

    allSubStr = sorted(allSubStr, key = len, reverse=True)

    for j in allSubStr:
        num = 0
        for i in seqs[1:]:
            if j in i.getSeq():
                num += 1
            else:
                break
        if num == len(seqs[1:]):
            return j

print sharedMotifs('test1')


print("--- %s seconds ---" % (time.time() - start_time))
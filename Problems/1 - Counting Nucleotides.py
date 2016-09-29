__author__ = 'paulsalvatore57'

#This was extremely easy, but I didn't know that these problems are timed.
#That makes these problems much more interesting, while at the same time much more stressful.
#I know the general problem I need to solve before the timer starts so I can do most of the question before starting.


def countNucleotides(file):
    num = {'A':0, 'C':0, 'G':0, 'T':0}
    file = open(file, 'r')
    for line in file:
        for char in line:
            if char in num:
                num[char] += 1
    return num

print countNucleotides('Q1 SEQUENCE')
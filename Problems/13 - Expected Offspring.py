__author__ = 'paulsalvatore57'

#Input will be a file with 6 numbers corresponding to the number of couples in a population with the genotypes:

    # AA-AA
    # AA-Aa
    # AA-aa
    # Aa-Aa
    # Aa-aa
    # aa-aa

#We want how many dominant phenotypes will be in the next generation, assuming each couple has two offspring

def AAAA(num):
    return 2*num

def AAAa(num):
    return 2*num

def AAaa(num):
    return 2*num

def AaAa(num):
    return 0.75*2*num

def Aaaa(num):
    return num

def aaaa(num):
    return 0


def howManyDomPheno(file):
    file = open(file, 'r')
    lnot = file.readline().split()
    l = []
    for i in lnot:
        l.append(int(i))
    return AAAA(l[0]) + AAAa(l[1]) + AAaa(l[2]) + AaAa(l[3]) + Aaaa(l[4]) + aaaa(l[5])

print howManyDomPheno('test1')
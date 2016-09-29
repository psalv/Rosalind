
####Has not been completed, I do not understand how you can have 0 composition since from my understanding the kmers are formed by the sequence itself.



#Will need to port this over to the sequence code when I am finished.


#First need to generate all kMers
#Then I need to lexicographically organize them.
#Then I need to determine how many times each kMer appears in the sequence and append this number to the list.


#Takes O(n) to build the kmers.
#Sorting can be done with merge sort in O(nlgn) time.
#Counting will take O(k*n) time


from Rosalind.SEQUENCE import *

def mergeSort(listOf):

    n = len(listOf)

    if n == 1:
        return listOf

    new1 = mergeSort(listOf[0:n / 2])
    new2 = mergeSort(listOf[n / 2:])

    return merge(new1, new2)

def merge(l1, l2):
    ans = []
    n1, n2 = len(l1), len(l2)

    i, j = 0, 0
    while len(ans) < n1 + n2:

        if j == n2:
            ans += l1[i:]
            return ans
        if i == n1:
            ans += l2[j:]
            return ans

        if l1[i] >= l2[j]:
            ans.append(l2[j])
            j += 1
        else:
            ans.append(l1[i])
            i += 1



def kMerComp(file, k=4):
    seq = FASTA_LOAD(file)

    kmers = []
    for i in xrange(len(seq.seq) - 3):
        kmers.append(seq.seq[i:i+4])

    kmers = mergeSort(kmers)

    kmerc = []

    print kmers

    match = None
    for i in kmers:
        if match == None:
            match = i
            num = 1
        elif i == match:
            num += 1
        else:
            kmerc.append(num)
            num = 1
            match = i

    c = ''
    for i in kmerc:
        c += str(i) + " "
    print c

    return kmerc


kMerComp('test1')



#I searched for the instances of each string using a rolling hash.
#Once I complied the list of the introns that I needed to remove I sorted this list (using merge sort).
#I then built the sequence based on the exons, creating a DNA_sequence object and translated to protein.



from Rosalind.SEQUENCE import *

class RollingHash(object):
    def __init__(self, seq, sub, base=256, p=4294967291):
        self.p = p
        self.base = base

        self.u = 0
        self.s = 0

        self.magic = None
        self.substring = sub
        self.text = seq
        self.textLen = len(self.text)
        self.wnd = len(sub)

        self.found = []

    def append(self, c):
        """Appends the rolling hash to include the character c."""
        self.u = (self.u * self.base + ord(c)) % self.p

    def skip(self, c):
        """Skip is to be performed before append.
        Removes the character c from the rolling hash."""
        self.u = (self.u - ord(c) * self.magic) % self.p

    def initializeValues(self):
        """Raises an exception unless both a substring and text have been specified.
        Initializes s, the hash value of the substring that we are looking for.
        Initializes t, the hash value of the first window frame of the text
        Initializes magic, a constant which will speed up the skip operation

        Note: if you want to skip after appending the -1 in the self.magic initialization need change to a zero."""
        if self.substring == None or self.text == None:
            raise ValueError("Need to initialize inputs.")

        for i in xrange(self.wnd):
            self.u = (self.u * self.base + ord(self.text[i])) % self.p
            self.s = (self.s * self.base + ord(self.substring[i])) % self.p

        self.magic = pow(self.base, self.wnd - 1) % self.p

    def checkCorrect(self, pos):
        """Checks if a presumptive positive is a true positive O(len(substring)).
        False positives should occur 1/p times, so with a large p value they will not affect the amortized runtime."""
        if self.u != self.s:
            return False
        elif self.text[pos:pos + self.wnd] == self.substring:
            return True
        else:
            return False

    def findInstances(self, toPrint=True):
        """Finds and prints (if True) all instances of the substring in the text."""
        self.initializeValues()

        for s in xrange(self.textLen - self.wnd + 1):

            if self.checkCorrect(s):
                self.found.append(s)

            if s < self.textLen - self.wnd:
                self.skip(self.text[s])
                self.append(self.text[s + self.wnd])
                self.u = (self.u + self.p) % self.p

        if toPrint:
            print self.found



def mergeSort(listOf):
    n = len(listOf)

    if n == 1:
        return listOf

    new1 = mergeSort(listOf[0:n / 2])
    new2 = mergeSort(listOf[n / 2:])

    return merge(new1, new2)

def merge(l1, l2):
    """Modified to sort by the first value in a tuple."""
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

        if l1[i][0] >= l2[j][0]:
            ans.append(l2[j])
            j += 1
        else:
            ans.append(l1[i])
            i += 1



def findPositions(file):
    """Finds the positions of introns and builds and translates a protein sequence from an exon.

    For this code to work the FASTA file should be in the form: Full (unspliced) DNA sequence, followed by every instance of intron sequence.

    Finds the positions of the introns using a rolling hash and returns a list of introns of the form: [(start of intron, stop of intron), ... ]
    Uses merge sort to sort the list of introns. Does not account for if there are two overlapping introns."""

    #Creates a list of DNA_sequence objects starting with the full unspliced sequence, followed by all of the introns.
    seqs = FASTA_LOAD(file)

    #Uses a rolling hash to find all of the intron positions
    #toRemove is of form: [(start of intron, end of intron), (start of next intron, end of next intron)....]
    toRemove = []
    for i in xrange(1, len(seqs)):
        f = RollingHash(seqs[0].seq, seqs[i].seq)
        f.findInstances(False)
        for j in f.found:
            toRemove.append((j, j + f.wnd))

    print toRemove
    seq = seqs[0].seq

    withoutIntrons = ''

    #Merge sorts the list toRemove based on starting positions (does not account for overlaps)
    toRemove = mergeSort(toRemove)


    #Builds the spliced DNA sequence based on the sorted intron list
    fr = 0
    for i in toRemove:
        withoutIntrons += seq[fr:i[0]]
        fr = i[1]
    withoutIntrons += seq[fr:]

    #Translates the spliced DNA sequence
    DNAseq = DNA_sequence("DNA seq without introns.", withoutIntrons)
    print DNAseq.toProtein()



findPositions('test1')
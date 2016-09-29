__author__ = 'paulsalvatore57'



import urllib2



def RAW_LOAD(file):
    """Returns a sequence from a text file containing just raw nucleotide data"""
    file = open(file, 'r')
    ans = ''
    fasta = False
    for line in file:
        if line[0] == '>':
            if fasta:
                raise AssertionError('More than one FASTA file in raw data.')
            fasta = True
            continue
        line = line.rstrip()
        ans += line
    return ans



class DNA_sequence(object):

    def __init__(self, ID, sequence):

        self.seq = sequence.upper()
        self.ID = ID
        self.ORFs = set([])

    def givePair(self, nuc, RNA = False):
        """Returns the corresponding nucleotide pair, or RNA pair if RNA = True"""
        nuc = nuc.upper()
        assert nuc in 'ATGC'

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

    def whichAminoAcid(self, codon):
        """Returns corresponding amino acid for a codon."""
        codon = codon.upper()
        codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",\
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",\
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",\
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",\
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",\
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",\
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",\
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",\
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",\
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",\
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",\
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",\
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",\
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",\
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",\
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

        return codons[codon].upper()

    def findORF(self, complement = False):
        """Searches for the longest AUG to stop codon region of RNA (searches the complement as well).
        Returns a list of the form [Position of stop of longest ORF, length of ORF]."""

        longest = None
        if not complement:
            self.ORFs = set([])
            longest = self.findORF(True)

        if complement:
            seq = self.getComplement(True)
        else:
            seq = self.toRNA()

        spot = 0

        while True:

            try:
                start = seq.index('AUG')

            except ValueError:
                return longest

            spot += start

            try:
                protein = self.toProtein(True, seq)
                protein_length = len(protein)
                protein = set([protein])
                self.ORFs = self.ORFs.union(protein)

            except TypeError:
                seq = seq[start + 1:]
                continue

            if longest == None:
                longest = [spot, protein_length, complement]
                spot += 1

            elif protein_length > longest[1]:
                longest = [spot, protein_length, complement]

            seq = seq[start + 1:]

    def getORFs(self, toPrint = False):
        if toPrint:
            for ORF in self.ORFs:
                print ORF
        return self.ORFs

    def toProtein(self, first = True, seq = None):
        """Converts the DNA strand to protein. Uses the first possible ORF if first,
        Otherwise searches for the longest possible ORF and uses that one."""

        if seq == None:
            seq = self.toRNA()

        if first:

            try:
                pos = seq.index('AUG')
            except ValueError:
                pos = None

        else:

            fOR = self.findORF()
            longest = None
            for start in self.ORFs:
                if longest == None:
                    longest = start
                elif len(start) > len(longest):
                    longest = start
            return longest

        protein = 'M'

        if pos == None:
            return None

        while True:
            pos += 3

            try:
                next = self.whichAminoAcid(seq[pos:pos + 3])
            except KeyError:
                return None

            if next == 'STOP':
                return protein

            else:
                protein += next

    def toRNA(self):
        """Returns the RNA transcription of the sequence"""
        ans = ''
        for base in self.seq:
            if base == 'T':
                ans += 'U'
            else:
                ans += base
        return ans

    def getSeq(self):
        return self.seq

    def getID(self):
        return self.ID

    def findMotif(self, motif, toPrint = False):
        """Returns all of the positions of the motif in the DNA sequence"""
        motif = motif.upper()
        seq = self.seq
        positions = []
        last = 0
        while len(seq) >= len(motif):
            try:
                pos = seq.index(motif) + 1
                positions.append(pos + last)
                last = pos + last
                seq = seq[pos:]
            except ValueError:
                break

        if toPrint:
            for pos in positions:
                print 'Motif at position:', pos, '-', pos + len(motif) - 1

        return positions

    def getGC(self):
        """Returns the GC content of the sequence"""
        GC = 0
        for base in self.seq:
            if base in 'GC':
                GC += 1
        return GC/float(len(self.seq))

    def getComplement(self, RNA = False, reverse = True):
        """Returns the DNA (or RNA if True) complement strand to the sequence"""

        if reverse:
            length = len(self.seq)
            spot = 1
            ans = ''
            while spot <= length:
                ans += self.givePair(self.seq[-spot], RNA)
                spot += 1
        else:
            length = len(self.seq)
            spot = 0
            ans = ''
            while spot < length:
                ans += self.givePair(self.seq[spot], RNA)
                spot += 1
        return ans

    def isReverse(self, s1, s2):
        """Returns True if s1 is the reverse of s2, False if not"""
        if len(s1) != len(s2):
            return False
        for i in xrange(len(s1)):
            if s1[i] != s2[-i - 1]:
                return False
        return True

    def findRestrictionSites(self):
        """Returns all of the reverse palindromes up from 2 - 6 bps in length"""
        reverse = self.getComplement(False, False)
        sequence = self.getSeq()

        sites = []
        spot = 0
        while spot < len(sequence):
            for i in xrange(2, 7):
                try:
                    s1 = sequence[spot:spot + i]
                    s2 = reverse[spot+i:spot + 2*i]
                    if self.isReverse(s1, s2):
                        sites += [(spot + 1, i*2),]
                except ValueError:
                    continue
            spot += 1
        return sites

    def __str__(self):
        return self.ID



class Protein_sequence(object):

    def __init__(self, ID, sequence, acc, toMotif = False):

        self.seq = sequence.upper()
        self.ID = ID
        self.acc = acc
        self.cantBe, self.exactly, self.either, self.length = None, None, None, None

        #This builds the library for which positions can't be certain amino acids, and which can be one of many amino acids.
        #Also creates a library of which amino acid positions must be exactly certain ones.
        if toMotif:
            motif = self.seq
            self.cantBe, self.either, self.exactly = {}, {}, {}
            minus, start, stop = 0, None, None

            for aa in xrange(len(motif)):

                if motif[aa] == '(':
                    start = aa
                elif motif[aa] == ')':
                    stop = aa
                    self.cantBe[aa - minus - len(motif[start + 1:stop])] = motif[start + 1:stop]
                    minus += len(motif[start + 1:stop]) + 1
                    start = None

                elif motif[aa] == '[':
                    start = aa
                elif motif[aa] == ']':
                    stop = aa
                    self.either[aa - minus - len(motif[start + 1:stop])] = motif[start + 1:stop]
                    minus += len(motif[start + 1:stop]) + 1
                    start = None

                elif start == None:
                    self.exactly[aa - minus + 1] = motif[aa]

            #This determines the length of motif, remove superfluous amino acid exceptions/limitations and brackets.
            self.length = len(motif.translate(None, '()[]'))
            for i in self.cantBe:
                if len(self.cantBe[i]) > 1:
                    self.length -= len(self.cantBe[i]) - 1
            for i in self.either:
                if len(self.either[i]) > 1:
                    self.length -= len(self.either[i]) - 1

    def findMass(self):
        mass = 0

        AAs = {'A': 71.03711,
                'C': 103.00919,\
                'D': 115.02694,\
                'E': 129.04259,\
                'F': 147.06841,\
                'G': 57.02146,\
                'H': 137.05891,\
                'I': 113.08406,\
                'K': 128.09496,\
                'L': 113.08406,\
                'M': 131.04049,\
                'N': 114.04293,\
                'P': 97.05276,\
                'Q': 128.05858,\
                'R': 156.10111,\
                'S': 87.03203,\
                'T': 101.04768,\
                'V': 99.06841,\
                'W': 186.07931,\
                'Y': 163.06333}

        for A in self.seq:
            mass += AAs[A]
        return mass


    def getSeq(self):
        return self.seq

    def getID(self):
        return self.ID

    def getAccession(self):
        return self.acc

    def getExactly(self):
        if self.exactly == None:
            raise AssertionError('This protein sequence is not a motif.')
        return self.exactly

    def getEither(self):
        if self.either == None:
            raise AssertionError('This protein sequence is not a motif.')
        return self.either

    def getCantBe(self):
        if self.cantBe == None:
            raise AssertionError('This protein sequence is not a motif.')
        return self.cantBe

    def getLength(self):
        if self.length == None:
            raise AssertionError('This protein sequence is not a motif.')
        return self.length

    def findMotif(self, motif):
        """Returns all of the positions of the motif in the protein sequence.

        Conventions for motif entry:
        I used regular brackets for amino acids that position cannot be, and square brackets for amino acids that a positions an be any of.
        For instance: A(TA)A[TA] means that position 2 CANNOT be T or A, and position 4 CAN be T or A"""

        seq = self.seq
        motifPositions = []
        last = 1

        cantBe = motif.getCantBe()
        either = motif.getEither()
        exactly = motif.getExactly()
        length = motif.getLength()
        motif = motif.getSeq()

        #This is the main loop which will go through each candidate position, shortening the sequence as it goes and recording matching motifs.
        while len(seq) >= len(motif):

            try:

                #This determines where the first potential candidate is.
                #A case I have not yet accounted for is if the first amino acid is a NOT,
                if motif[0] == '[':
                    ind = []
                    for i in either[1]:
                        ind.append(seq.index(i))
                    pos = max(ind)
                elif motif[0] == '(':
                    raise NotImplementedError
                else:
                    pos = seq.index(motif[0])

                target = seq[pos:pos+length]

                #This section determines if each position corresponds with the acceptable parameters.
                #If not it will break and finish = False, so won't add to the motif positions list.
                finish = True
                for i in xrange(length):
                    if i + 1 in cantBe:
                        if target[i] in cantBe[i + 1]:
                            finish = False
                            break
                    elif i + 1 in either:
                        if target[i] not in either[i + 1]:
                            finish = False
                            break
                    else:
                        if exactly[i + 1] != target[i]:
                            finish = False
                            break

                if finish:
                    motifPositions.append(pos + last)

                last += pos + 1

                seq = seq[pos + 1:]

            except ValueError:
                break

        return motifPositions

    def __str__(self):
        return self.ID



def FASTA_LOAD_PROT(file):
    """Can load multiple fasta files from a single text document (given that the text document is of the form one accession number per line).
    Returns a list of Protein_sequence objects corresponding to each FASTA entry."""

    file = open(file, 'r')
    acces = []
    for line in file:
        acces.append(line.rstrip())
    proteins = []
    for ACC in acces:
        FASTA = 'http://www.uniprot.org/uniprot/' + ACC + '.fasta'
        try:
            response = urllib2.urlopen(FASTA)
        except urllib2.URLError:
            print '\nURL ERROR\n  INVALID ACCESSION: ' + ACC + '\n'
            continue
        ID = None
        seq = ''
        for line in response:
            if line[0] == '>':
                ID = line
            else:
               seq += line.rstrip()
        proteins.append(Protein_sequence(ID, seq, ACC))
    return proteins



def FASTA_LOAD(file):
    """Can load multiple fasta files from a single text document.
    Returns a list of DNA_sequence objects corresponding to each FASTA entry."""

    file = open(file, 'r')
    seq = ''
    sequences = []
    for line in file:
        line = line.rstrip()
        if line[0] == '>':
            if seq != '':
                sequences += [DNA_sequence(ID, seq),]
            ID = line
            seq = ''
        else:
            seq += line

    sequences += [DNA_sequence(ID, seq),]

    if len(sequences) == 1:
        return sequences[0]
    else:
        return sequences


from Rosalind.SEQUENCE import *


def proteinMass():
    """Uses the protein sequence class to compute the mass of the given protein sequence."""
    seq = RAW_LOAD('test1')
    prot = Protein_sequence(None, seq, None)
    print prot.findMass()

proteinMass()
__author__ = 'paulsalvatore57'

from Rosalind.SEQUENCE import *

def proteinify(file):
    toConvert = DNA_sequence(None, RAW_LOAD(file))
    print toConvert.toProtein(False)
    print '\n'
    # toConvert.findORF()
    # toConvert.getORFs(True)


proteinify('test1')



#So I was just about to pull my hair out on this one, but I think I've gotten a couple valuable lessons out of it.
#The first being that stepping away from a problem can be extremely helpful, it allows you to think about the problem in a different light.
#Secondly, I learned that if you have all the pieces for the answer, no one cares how ou actually get it.
#I wanted my program to retranslate the DNA, but I already had all of the possible fragments.
#The answer would be identical to the longest, so why would I not just pick the longest and use that as my answer, saves me a lot of headaches.
#At this point I probably have some superfluous code from my attempt which I could go clean but I'm not afraid of breaking something.
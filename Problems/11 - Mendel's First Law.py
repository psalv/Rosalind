__author__ = 'paulsalvatore57'


#Given a population with k homo-dominant, m hetero, and n homo-recessive.
#What is the probability of taking two individuals at random and creating a dominant phenotype?

#Events that lead to this:
    #1) Homo-dom 2) Homo-dom
    #1) Homo-dom 2) Hetero
    #1) Homo-dom 2) Homo-rec

    #1) Hetero (50%) 2) Hetero
    #1) Hetero (50%) 2) Hetero (50%)
    #1) Hetero (50%) 2) Homo-rec
    #1) Hetero 2) Homo-Dom

    #1) Homo-rec 2) Homo-Dom
    #1) Homo-rec 2) Hetero (50%)


def domPhenotype(k, m, n):
    """Takes in k (number of homo Dominants), m (number of hetero) and n (number of homo recessive) for a population.
    Returns the probability that any two pairs, chosen at random, will yield a phenotypically dominant offspring."""
    total = float(k + m + n)
    chance = 0

    chance += k/total * (k-1)/(total - 1)
    chance += k/total * (m)/(total - 1)
    chance += k/total * (n)/(total - 1)

    chance += (0.5)*(m/total) * (m - 1)/(total - 1)
    chance += (0.5)*(m/total) * (0.5)*(m - 1)/(total - 1)
    chance += (0.5)*(m/total) * (n)/(total - 1)
    chance += (m/total) * (k)/(total - 1)

    chance += (n/total) * (k)/(total - 1)
    chance += (n/total) * (0.5)*(m)/(total - 1)

    return chance

print domPhenotype(26, 30, 24)


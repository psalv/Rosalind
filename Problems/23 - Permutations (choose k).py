
import math

def permutationsWithK(x, y):
    """Number of permutations of y elements from x, mod 10^6."""
    x = float(x)
    return math.factorial(x) / (math.factorial(x - y)) % 1000000

print permutationsWithK(95, 8)
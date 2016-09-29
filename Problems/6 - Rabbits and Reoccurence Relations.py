__author__ = 'paulsalvatore57'

#I relied heavily on the test case for this set, but the premise is:
    #Same as a fibonacci sequence but intead of fn = fn-1 + fn-2, the sequence is fn = fn-1 + k*fn-2


def altFib(n, k):
    fib = [1, 1]
    for i in xrange(n - 2):
        hold = fib[1]
        fib[1] = fib[1] + k*fib[0]
        fib[0] = hold
    return fib[1]

print altFib(100, 2)
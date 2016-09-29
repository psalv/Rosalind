__author__ = 'paulsalvatore57'

def altFib(n, m):
    start = [1, 1, 1]

    zeros = [0]*(m-1)

    fib = zeros + start


    while len(fib) < n + m:


        num = fib[-1]+fib[-2]


        # print fib
        # print 'Sum of last two:', num
        # print 'To be subtracted:', fib[-m - 1]

        fib.append(num - fib[-m - 1])

    return fib

print altFib(89, 19)


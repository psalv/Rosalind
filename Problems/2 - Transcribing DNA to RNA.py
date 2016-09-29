__author__ = 'paulsalvatore57'


def transcribe(file):
    file = open(file, 'r')
    ans = ''
    for line in file:
        for char in line:
            if char == 'T':
                ans += 'U'
            else:
                ans += char
    return ans

transcribe('Q2 SEQUENCE')
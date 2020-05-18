import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #do NOT actually construct the string, that's silly.
    #get the number of times the s will appear in the string.
    mults = int(n/len(s))
    #get the length of s after being truncated at the end.
    tail = n%len(s)
    count = s.count('a')*mults
    tail_str = s[0:tail]
    count += tail_str.count('a')
    return count
if __name__ == '__main__':
    s = 'aba'

    n = 10

    result = repeatedString(s, n)
    print(result)

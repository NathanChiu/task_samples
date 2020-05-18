import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = {}
    for char in s1:
        d[char] = True
    # print(d)
    for char in s2:
        if char in d.keys():
            return "YES"
    return "NO"
if __name__ == '__main__':
    q = 2
    s1s = ['hello', 'hi']
    s2s = ['world', 'world']
    for q_itr in range(q):
        s1 = s1s[q_itr]
        s2 = s2s[q_itr]
        result = twoStrings(s1, s2)
        print(result)

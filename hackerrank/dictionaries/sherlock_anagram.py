import math
import os
import random
import re
import sys
import textwrap

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    #use a sliding window, and check its existence in a dictionary.
    d = {}
    for window_length in range(1,len(s)):
        candidates = []
        #current window is i long. if window is 2 long, and string is 4 long, have 3 candidates.
        #start at front of string.
        for pos in range(len(s)+1-window_length):
            candidates.append(s[pos:pos + window_length])
        # candidates = textwrap.wrap(s, i)
        for item in candidates:
            #if chunks are not same size as what we are looking at, disregard
            # if len(item) == window_length:
            sorted_item = "".join(sorted(item))
            if sorted_item not in d.keys():
                d[sorted_item] = 1
            else:
                d[sorted_item] +=1
    # print(sum(d.values()) - len(d.values()))
    # print(d)
    #get the number of possible pairs given that X of the matching items exist.
    #eg. 1 item = no pairs, 2 items = 1 pair, 3 items = 3 pairs, 4 items = 6 pairs, etc.
    sum = 0
    for val in d.values():
        for i in range(val):
            sum += i
    return sum
if __name__ == '__main__':
    q = 2
    ss = ['ifailuhkqq', 'kkkk']
    for q_itr in range(q):
        s = ss[q_itr]
        result = sherlockAndAnagrams(s)
        print(result)

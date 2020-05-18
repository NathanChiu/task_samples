import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #people can end up arbitrarily backwards, but only 2 forwards at most.
    #start from the front, seeing the ones we expect.
    #start with a sorted list of all members.
    cands = [*range(1,len(q)+1)]
    jumps = 0
    ind = 1
    #go through q, making note of how many jumps it had to have taken for the current member to be ahead of the expected member.
    for member in q:
        #it is the next member we expect
        if member == cands[0]:
            cands.remove(member)
        #cannot be more than 2 ahead of initial position. terminate.
        elif (member - ind) > 2:
            # print(member, cands[0])
            print('Too chaotic')
            return
        #it is not the member we expect. eg, member 5 when expected member 3.
        #get the number of items between the expected member and the seen member.
        elif (member - ind) <= 2:
            num_items = len(cands[:cands.index(member)])
            # print(num_items)
            # jumps += member - cands[0]
            jumps += num_items
            cands.remove(member)
        ind += 1
    print(jumps)
if __name__ == '__main__':
    t = 4
    ns = [5, 5, 8, 8]
    qs = [[2, 1, 5, 3, 4], [2, 5, 1, 3, 4], [5, 1, 2, 3, 7, 8, 6, 4], [1, 2, 5, 3, 7, 8, 6, 4]]
    for t_itr in range(t):
        n = ns[t_itr]
        q = qs[t_itr]
        minimumBribes(q)

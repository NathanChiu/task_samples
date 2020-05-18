import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    second = defaultdict(lambda:0)
    third = defaultdict(lambda:0)
    count = 0
    for item in arr:
        #if the triplet is completed, add the number of permutations to the total.
        if item in third.keys():
            count += third[item]
        #if the item is a second item in a triplet, prepare the total number of permutations so far.
        if item in second.keys():
            third[item*r] += second[item]
        #assume that the item can always be a first item in a triplet. add 1 more to the count for possible triplets
        second[item*r] += 1
    return count

if __name__ == '__main__':
    n = 6
    r = 3
    arr = [1, 3, 9, 9, 27, 81]
    ans = countTriplets(arr, r)
    print(ans)

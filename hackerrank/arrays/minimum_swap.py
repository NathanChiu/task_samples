import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #start at front of list, for entire list
    i = 0
    count = 0
    while i < len(arr):
        #correct item in correct spot
        if arr[i] == i+1:
            i += 1
        #incorrect item in incorrect spot, put this item in place.
        else:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            count += 1
    return count
if __name__ == '__main__':
    n = 7
    # arr = [1, 3, 5, 2, 4, 6, 7]
    arr = [7, 5, 6, 4, 3, 2, 1]
    res = minimumSwaps(arr)
    print(res)

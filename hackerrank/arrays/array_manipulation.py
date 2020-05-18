import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1) #n+1 for 'dummy' spot
    #think about an energy landscape, only need to record changes in height.
    for a, b, k in queries:
        #add the beginning of a peak
        arr[a-1] += k
        #add the end of a peak. if b == len(queries), then the descent never comes, add it to the dummy index.
        arr[b] -= k
    #remove the dummy spot
    arr = arr[:-1]
    #now, traverse along this height gradient and find the maximum height.
    height = 0
    max = 0
    for item in arr:
        height += item
        if height > max:
            max = height
    return max


if __name__ == '__main__':
    n = 5
    m = 3
    queries = [[1, 2, 100],[2, 5, 100], [3, 4, 100]]
    result = arrayManipulation(n, queries)
    print(result)

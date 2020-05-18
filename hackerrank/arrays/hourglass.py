import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    num_hgs = (len(arr)-2)*(len(arr[0])-2)
    max_sum = None
    #the xspace
    for i in range(1, len(arr)-1):
        #the yspace
        for j in range(1, len(arr[0])-1):
            hg_sum = 0
            hg_sum += sum(arr[i-1][j-1:j+2])
            hg_sum += sum(arr[i+1][j-1:j+2])
            hg_sum += arr[i][j]
            if max_sum == None or hg_sum > max_sum:
                max_sum = hg_sum
    return max_sum

if __name__ == '__main__':
    in_str = '1 1 1 0 0 0 \n\
              0 1 0 0 0 0 \n\
              1 1 1 0 0 0 \n\
              0 0 2 4 4 0 \n\
              0 0 0 2 0 0 \n\
              0 0 1 2 4 0'
    strs = in_str.split('\n')
    arr = []
    for item in strs:
        arr.append(list(map(int, item.rstrip().lstrip().split())))
    # for _ in range(6):
    #     arr.append(list(map(int, in_str.rstrip().split())))

    result = hourglassSum(arr)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    count = 0
    is_below = False
    for step in range(n):
        if s[step] == 'U':
            height += 1
        if s[step] == 'D':
            height -= 1
        if height < 0:
            is_below = True
        #if at sea level, and was below
        elif height == 0 and is_below:
            count += 1
            is_below = False
        else:
            is_below = False
    return count
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = 8
    n = 12
    # s = 'UDDDUDUU'
    s = 'DDUUDDUDUUUD'
    result = countingValleys(n, s)
    print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

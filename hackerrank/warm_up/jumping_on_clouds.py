import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    last_pos = len(c) - 1
    pos = 0
    jumps = 0
    while pos < last_pos:
        # if at the second last position, don't check indices.
        if last_pos - pos <= 2:
            pos = last_pos
        #prioritize jumping 2.
        elif c[pos+2] == 0:
            pos += 2
        #can always win game, so the next one MUST be free.
        else:
            pos += 1
        jumps += 1
        # print(pos)
    return jumps

if __name__ == '__main__':
    n = 6

    c = [0, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(c)
    print(result)

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]
if __name__ == '__main__':
    n = 5
    d = 4
    a = '1 2 3 4 5'
    a = list(map(int, a.rstrip().split()))

    result = rotLeft(a, d)
    print(result)

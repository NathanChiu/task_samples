import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_items = set(ar)
    pairs = 0
    for item in unique_items:
        pairs += int(ar.count(item)/2)
    return pairs

if __name__ == '__main__':
    n = 10
    ar = [0, 2, 4, 1, 2, 5, 4, 3, 3, 2]
    print(ar)
    result = sockMerchant(n, ar)
    print(result)

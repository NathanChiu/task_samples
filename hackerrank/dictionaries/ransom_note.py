import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = {}
    for item in magazine:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    for item in note:
        if item not in d or d[item] == 0:
            print('No')
            return
        else:
            d[item] -= 1
    print('Yes')
if __name__ == '__main__':
    m = 6
    n = 5
    magazine = 'give me one grand today night'.rstrip().split()

    note = 'give one grand today'.rstrip().split()

    checkMagazine(magazine, note)

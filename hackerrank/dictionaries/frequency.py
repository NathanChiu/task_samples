import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    d = defaultdict(lambda:0)
    f = defaultdict(lambda:0)
    results = []
    for op, x in queries:
        if op == 1:
            d[x] += 1
            #there is an item with frequency d[x]
            f[d[x]] += 1
            #remove an item with frequency d[x]-1
            if f[d[x]-1] > 0:
                f[d[x]-1] -= 1
        elif op == 2:
            if d[x] > 0:
                d[x] -= 1
                f[d[x]] += 1
                if f[d[x]+1] > 0:
                    f[d[x]+1] -= 1
        elif op == 3:
            if f[x] != 0:
                results.append(1)
            else:
                results.append(0)
    # print(results)
    return results
    # print(queries)
if __name__ == '__main__':
    q = 10
    queries = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
    ans = freqQuery(queries)
    print(ans)

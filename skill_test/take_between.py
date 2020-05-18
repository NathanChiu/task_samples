# import sys;
#
# def main():
#     inStr = sys.stdin.readline().rstrip('\n')
#     leftSep = sys.stdin.readline().rstrip('\n')
#     rightSep = sys.stdin.readline().rstrip('\n')
#     takeUntilEndIfRightMissing = True if (sys.stdin.readline().rstrip('\n')=="1") else False
#
#     output = TakeBetween(inStr, leftSep, rightSep, takeUntilEndIfRightMissing);
#
#     sys.stdout.write(output)
#
# def TakeBetween(inStr, left, right, takeUntilEndIfRightMissing):
#     #index of the end of first occurence of left.
#     if inStr.find(left) == -1:
#         return str(None)
#     l_ind = inStr.find(left) + len(left)
#     new_str = inStr[l_ind:]
#     if takeUntilEndIfRightMissing:
#         return new_str
#     else:
#         if new_str.find(right) == -1:
#             return str(None)
#         return new_str[:new_str.find(right)]
#     #return inStr
#
# main()

def getGrad(value):
    thresholds = {}
    thresholds[1E15] = 'Q'
    thresholds[1E12] = 'T'
    thresholds[1E9] = 'B'
    thresholds[1E6] = 'M'
    thresholds[1E3] = 'K'
    # print(thresholds.keys())
    for t in thresholds.keys():
        if value >= t:
            return t, thresholds[t]

print(getGrad(50000000))

#
# Failed for Empty Delim: Failed with [] rather than [exception]

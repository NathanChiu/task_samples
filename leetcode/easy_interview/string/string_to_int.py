import re

class Solution:
    def myAtoi(self, s):
        matches = re.search("^\s*([-+]?[0-9]+)", s)
        if matches:
            groups =  matches.groups()
            num = int(groups[0])
        else:
            num = 0
        if num < -(2**31):
            num = -(2**31)
        if num > 2**31-1:
            num = 2**31-1
        return num
            # print(match)
        # print(matches.group())
sol = Solution()
s = "-4193 with words"
# s = "words and -987"
print(sol.myAtoi(s))

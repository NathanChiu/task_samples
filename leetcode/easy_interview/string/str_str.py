import re

class Solution:
    def strStr(self, haystack, needle):
        if not str:
            return 0
        matches = re.search("("+needle+")", haystack)
        if matches:
            span = matches.span()[0]
            return span
        else:
            return -1


sol = Solution()
h = "helloll"
n = "ll"
print(sol.strStr(h, n))

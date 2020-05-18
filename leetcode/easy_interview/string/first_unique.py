from collections import defaultdict

class Solution:
    def firstUniqChar(self, s):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in s:
            if d[c] == 1:
                return s.find(c)
        else:
            return -1

# s = "leetcode"
s = "llss"
sol = Solution()
print(sol.firstUniqChar(s))

from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for key, val in d.items():
            if val == 1:
                return key


sol = Solution()
A = [4,1,2,1,2]
print(sol.singleNumber(A))

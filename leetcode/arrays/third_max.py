from collections import defaultdict

class Solution:
    def thirdMax(self, nums):
        d = defaultdict(bool)
        for item in nums:
            d[item] = True
        sorted_nums = sorted(list(d.keys()), reverse=True)
        if len(sorted_nums) < 3:
            return sorted_nums[0]
        else:
            return sorted_nums[2]

sol = Solution()
A = [2, 2, 3, 1]
print(sol.thirdMax(A))

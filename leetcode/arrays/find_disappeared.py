from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums):
        if not nums:
            return []
        d = defaultdict(bool)
        for num in nums:
            d[num] = True
        missing = []
        for i in range(1, len(nums)+1):
            if not d[i]:
                missing.append(i)
        return missing


sol = Solution()
A = [1, 1]
# A = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(A))

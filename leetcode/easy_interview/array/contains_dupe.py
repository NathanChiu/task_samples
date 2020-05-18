class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for item in nums:
            d[item] = True
        if len(d.keys()) == len(nums):
            return False
        else:
            return True

A = [1,1,1,3,3,4,3,2,4,2]
sol = Solution()
print(sol.containsDuplicate(A))

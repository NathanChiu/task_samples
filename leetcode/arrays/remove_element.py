class Solution:
    def removeElement(self, nums, val):
            while val in nums:
                nums.remove(val)
            return len(nums)

sol = Solution()
A = [0,1,2,2,3,0,4,2]
element = 2
sol.removeElement(A, element)
print(A)

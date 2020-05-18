class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return
        target = nums[0]
        index = 1
        while index < len(nums):
            if nums[index] == target:
                del nums[index]
                continue
            target = nums[index]
            index += 1






# A = [0,0,1,1,1,2,2,3,3,4]
A = [1, 1]
sol = Solution()
sol.removeDuplicates(A)
print(A)

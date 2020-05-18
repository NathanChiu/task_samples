class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        num_zeros = 0
        while ind < len(nums):
            if nums[ind] == 0:
                del nums[ind]
                num_zeros += 1
                continue
            ind += 1
        for _ in range(num_zeros):
            nums.append(0)

sol = Solution()
A = [0,1,0,3,12]
sol.moveZeroes(A)
print(A)

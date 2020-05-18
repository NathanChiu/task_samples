class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            del nums[-1]

sol = Solution()
A = [1,2,3,4,5,6,7]
k = 3
sol.rotate(A,k)
print(A)

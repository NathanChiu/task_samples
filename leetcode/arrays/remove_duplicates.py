class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        to_del = []
        prev_num = nums[0]
        for num in nums[1:]:
            if prev_num == num:
                to_del.append(num)
            else:
                prev_num = num
        for num in to_del:
            nums.remove(num)
        return len(nums)

sol =  Solution()
A = [0,0,1,1,1,2,2,3,3,4]
sol.removeDuplicates(A)
print(A)

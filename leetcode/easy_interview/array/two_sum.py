from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for num, count in list(d.items()):
            complement = target - num
            if d[complement]:
                if complement == num:
                    if count >= 2:
                        #same number, two different indices.
                        #find first one.
                        i = nums.index(num)
                        del nums[i]
                        j = nums.index(complement)
                        if j >= i:
                            j += 1
                        return [i, j]
                    else:
                        continue
                else:
                    #different numbers.
                    return [nums.index(num), nums.index(complement)]

# A = [2, 7, 11, 15, 2]
# t = 4
A = [2, 5, 5, 11]
t = 10
sol = Solution()
print(sol.twoSum(A, t))

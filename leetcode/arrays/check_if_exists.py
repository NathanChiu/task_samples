from collections import defaultdict

class Solution:
    def checkIfExist(self, arr):
        dict = defaultdict(int)
        for num in arr:
            dict[num] += 1
        for num in arr:
            if dict[2*num] != 0:
                if num == 0:
                    if dict[0] >= 2:
                        return True
                    else:
                        continue
                return True
        return False
sol = Solution()
# A = [0,7,1,14,11]
# A = [-2,0,10,-19,4,6,-8]
A = [0,0]
# A = [-20,8,-6,-14,0,-19,14,4]
print(sol.checkIfExist(A))

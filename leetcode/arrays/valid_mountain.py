class Solution:
    def validMountainArray(self, A):
        if len(A) <= 2:
            return False
        prev_num = A[0]
        if A[1] - A[0] > 0:
            climbing = True
        elif A[1] - A[2] < 0:
            climbing = False
        else:
            return False
        for num in A[1:]:
            # print(prev_num, num)
            if climbing:
                if num-prev_num > 0:
                    pass
                elif num-prev_num < 0:
                    climbing = False
                else:
                    return False
            elif not climbing:
                if num-prev_num < 0:
                    pass
                else:
                    return False
            else:
                return False
            prev_num = num
        if climbing:
            return False
        else:
            return True


sol = Solution()
# A = [3,5,5]
# A = [0,3,2,1]
A = [2, 1]
print(sol.validMountainArray(A))

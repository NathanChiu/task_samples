class Solution:
    def reverse(self, x):
        s = str(x)
        s = "".join(reversed(s))
        if x < 0:
            # print(s[-1] + s[:-1])
            s = s[-1] + s[:-1]
        num = int(s)
        if -(2**31) < num < 2**31-1:
            return num
        else:
            return 0
        # return int(s)


sol = Solution()
num = -123
print(sol.reverse(num))

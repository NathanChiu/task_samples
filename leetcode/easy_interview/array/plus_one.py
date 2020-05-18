class Solution:
    def plusOne(self, digits):
        num = int("".join(map(str, digits)))+1
        final_list = [int(char) for char in str(num)]
        return final_list

sol = Solution()
A = [1,2,3]
print(sol.plusOne(A))

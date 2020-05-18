class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
sol = Solution()
s = ["h","e","l","l","o"]
sol.reverseString(s)
print(s)

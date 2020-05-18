class Solution:
    def sortedSquares(self, A):
        squares = list(map(lambda x: x**2, A))
        squares.sort()
        return squares

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))

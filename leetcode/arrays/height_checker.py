class Solution:
    def heightChecker(self, heights):
        packed_heights = zip(heights, sorted(heights))
        out_of_place = [0 if x == y else 1 for x, y in packed_heights]
        return sum(out_of_place)

sol = Solution()
# A = [5,1,2,3,4]
A = [5,2,1,3,4]
print(sol.heightChecker(A))

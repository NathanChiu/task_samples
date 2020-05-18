class Solution:
    def sortArrayByParity(self, A):
        evens = []
        odds = []
        for item in A:
            if item%2 == 0:
                evens.append(item)
            else:
                odds.append(item)
        return evens+odds


A = [3,1,2,4]
sol = Solution()
print(sol.sortArrayByParity(A))

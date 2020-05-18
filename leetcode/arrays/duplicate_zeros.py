class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        max_len = len(arr)
        indices = [i for i, item in enumerate(arr) if item == 0]
        #insert reversed, so don't have to change indices as we add.
        indices.reverse()
        for i in indices:
            arr.insert(i, 0)
        del arr[max_len:]

A = [1,0,2,3,0,4,5,0]
sol = Solution()
sol.duplicateZeros(A)
print(A)

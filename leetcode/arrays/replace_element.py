class Solution:
    def replaceElements(self, arr):
        reverse_arr = arr
        reverse_arr.reverse()
        final_arr = [-1]
        curr_max = 0
        for item in reverse_arr[:-1]:
            if item > curr_max:
                curr_max = item
            final_arr.append(curr_max)
        final_arr.reverse()
        return final_arr


A = [17,18,5,4,6,1]
sol = Solution()
print(sol.replaceElements(A))

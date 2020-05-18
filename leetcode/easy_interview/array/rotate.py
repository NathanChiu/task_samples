class Solution:

    def rotate(self, matrix):
        length = len(matrix)
        num_layers = int((length + 1 )/2)
        for ring in range(num_layers):
            for i in range(length-2*ring-1):
                temp = matrix[0+ring][i+ring]
                matrix[0+ring][i+ring] = matrix[length-1-i-ring][0+ring]
                matrix[length-1-i-ring][0+ring] = matrix[length-1-ring][length-1-i-ring]
                matrix[length-1-ring][length-1-i-ring] = matrix[i+ring][length-1-ring]
                matrix[i+ring][length-1-ring] = temp

# A = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

A = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
sol = Solution()
sol.rotate(A)
print(A)

import numpy as np
from collections import defaultdict

class Solution:
    def getRow(self, board, ind):
        return board[ind, :]
    def getCol(self, board, ind):
        return board[:, ind]
    def getSquare(self, board, ind):
        #0 1 2
        #3 4 5
        #6 7 8
        x = int(ind / 3)
        y = ind % 3
        x_center = 1 + x*3
        y_center = 1 + y*3
        return board[x_center-1:x_center+2,y_center-1:y_center+2]
    def checkRepeat(self, d):
        for key, val in d.items():
            if val > 1 and key != '.':
                return False
        return True

    def isValidSudoku(self, board):
        board = np.array(board)
        length = 9
        d = defaultdict(int)
        for i in range(9):
            #check row:
            d.clear()
            row = self.getRow(board, i)
            for item in row:
                d[item] += 1
            if not self.checkRepeat(d):
                return False
            d.clear()
            col = self.getCol(board, i)
            for item in col:
                d[item] += 1
            if not self.checkRepeat(d):
                return False
            d.clear()
            square = self.getSquare(board, i)
            square = square.flatten('C')
            for item in square:
                d[item] += 1
            if not self.checkRepeat(d):
                return False
        return True
        # square = self.getSquare(board, 0)
        # square = square.flatten('C')
        # print(square)
            # print(self.getSquare(board, 0).flatten())
        # print(self.getSquare(board, 5))

sol = Solution()
# A = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
A = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(A))

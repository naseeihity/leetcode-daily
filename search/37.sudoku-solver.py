#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self._solve(board)

    def _solve(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == '.':
                    for c in range(0, 9):
                        if self._isValid(board, i, j, self.numbers[c]):
                            board[i][j] = self.numbers[c]
                            if self._solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def _isValid(self, board, i, j, c):
        for k in range(0, 9):
            if board[k][j] != '.' and board[k][j] == c:
                return False
            if board[i][k] != '.' and board[i][k] == c:
                return False
            if board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] != '.' and board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] == c:
                return False

        return True
        # @lc code=end

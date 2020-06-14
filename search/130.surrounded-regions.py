#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start


class Solution:
    def __init__(self):
        self.visited = set()

    def dfs(self, board, i, j):
        if 0 == i or i == len(board)-1 or 0 == j or j == len(board[0]) - 1:
            return False

        if (i, j) not in self.visited:
            self.visited.add((i, j))
            a, b, c, d = True, True, True, True
            if board[i-1][j] == 'O':
                a = self.dfs(board, i-1, j)
            if board[i+1][j] == 'O':
                b = self.dfs(board, i+1, j)
            if board[i][j-1] == 'O':
                c = self.dfs(board, i, j-1)
            if board[i][j+1] == 'O':
                d = self.dfs(board, i, j+1)

            return a and b and c and d

        return True

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        h = len(board)
        w = len(board[0])

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    should_change = self.dfs(board, i, j)

                    if should_change:
                        for a, b in self.visited:
                            board[a][b] = 'X'
                    self.visited.clear()


# @lc code=end

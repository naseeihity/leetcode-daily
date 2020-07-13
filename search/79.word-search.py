#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start


class Solution:
    def search(self, x, y, d):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or self.word[d] != self.board[x][y]:
            return False
        elif d == len(self.word) - 1:
            return True

        cur = self.board[x][y]
        self.board[x][y] = 0

        found = self.search(x-1, y, d+1) or self.search(x+1, y, d +
                                                        1) or self.search(x, y-1, d+1) or self.search(x, y+1, d+1)

        self.board[x][y] = cur

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.word = word
        self.board = board
        self.m = m
        self.n = n

        for i in range(m):
            for j in range(n):
                if self.search(i, j, 0):
                    return True

        return False

# @lc code=end

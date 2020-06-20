#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])

        ans = 0

        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    ans = max(ans, dp[i][j])

        return ans * ans

# @lc code=end

#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                for a in range(i, m):
                    dp[0][a] = 0
                break

        for j in range(n):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                for b in range(j, n):
                    dp[b][0] = 0
                break

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]
# @lc code=end

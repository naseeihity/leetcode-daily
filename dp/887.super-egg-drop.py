#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1

        return m
# @lc code=end

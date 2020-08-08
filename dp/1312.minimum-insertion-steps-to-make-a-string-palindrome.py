#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(2, n+1):
            i = 0
            for j in range(l-1, n):
                dp[i][j] = dp[i+1][j -
                                   1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1])+1
                i += 1

        return dp[0][n-1]
# @lc code=end

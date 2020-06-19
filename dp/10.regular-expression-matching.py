#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start


class Solution:
    # dp
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}

                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
    # Recursion
    # def isMatch(self, s: str, p: str) -> bool:
    #     if not p:
    #         return not s

    #     first_match = bool(s) and p[0] in {s[0], '.'}

    #     if len(p) >= 2 and p[1] == '*':
    #         return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
    #     else:
    #         return first_match and self.isMatch(s[1:], p[1:])
# @lc code=end

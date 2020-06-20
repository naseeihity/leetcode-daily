#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [0 for _ in range(size+1)]
        dp[0] = 1

        for i in range(1, size+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break

        return dp[size]
# @lc code=end

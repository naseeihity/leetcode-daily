#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = 2
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]

        for i in range(n):
            for kk in range(1, k+1):
                if i == 0:
                    dp[i][kk][0] = 0
                    dp[i][kk][1] = -prices[i]
                else:
                    dp[i][kk][0] = max(
                        dp[i-1][kk][0], dp[i-1][kk][1]+prices[i])
                    dp[i][kk][1] = max(
                        dp[i-1][kk][1], dp[i-1][kk-1][0]-prices[i])
        print(dp[n-1][k][0])
        return dp[n-1][k][0]


test = Solution()
test.maxProfit([1, 2, 3, 4, 6])
# @lc code=end

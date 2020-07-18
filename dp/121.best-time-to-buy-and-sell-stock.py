#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        sell, hold = 0, -prices[0]

        for i in range(1, n):
            sell = max(sell, hold + prices[i])
            hold = max(hold, -prices[i])

        return sell

    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0

    #     k = len(prices)
    #     dp = [[0 for _ in range(2)] for _ in range(k)]
    #     dp[0][0], dp[0][1] = 0, -prices[0]

    #     for i in range(1, k):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    #         dp[i][1] = max(dp[i-1][1], -prices[i])

    #     return dp[k-1][0]
# @lc code=end

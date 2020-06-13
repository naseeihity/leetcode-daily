
import sys
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0

        n = len(prices)
        # k大于n/2时，相当于无限次
        max_profit = 0
        if k >= n / 2:    # to avoid memory error
            for i in range(1, n):
                # same to Stock II
                max_profit += max(prices[i] - prices[i-1], 0)
            return max_profit

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

        return dp[n-1][k][0]

# @lc code=end

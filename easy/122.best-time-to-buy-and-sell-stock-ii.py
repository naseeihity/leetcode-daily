#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i, p in enumerate(prices[:-1]):
            if (p >= prices[i+1]):
                continue
            profit += prices[i+1] - p

        return profit
# @lc code=end

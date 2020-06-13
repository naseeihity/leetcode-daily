#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        k = len(prices)
        hold0, hold1 = 0, -prices[0]

        for i in range(1, k):
            hold0, hold1 = max(
                hold0, hold1+prices[i]), max(hold1, hold0-prices[i])

        return hold0
# @lc code=end

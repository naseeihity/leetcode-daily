#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if self.cache and self.cache[n]:
            return self.cache[n]

        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.cache[n]
# @lc code=end

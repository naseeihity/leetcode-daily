#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        x, y = 1, 2

        for _ in range(2, n):
            x, y = y, x + y

        return y
# @lc code=end

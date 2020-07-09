#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        a, b, ans = abs(dividend), abs(divisor), 0

        while a >= b:
            x = 0
            while a >= b << (x+1):
                x += 1

            ans += 1 << x
            a -= b << x

        return min(ans if sig else -ans, 2147483647)
# @lc code=end

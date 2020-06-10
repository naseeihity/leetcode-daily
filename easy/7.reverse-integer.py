#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31 - 1
        min = -(2**31)

        strx = str(abs(x))
        strx_reverse = int(strx[::-1])
        result = strx_reverse if x > 0 else -strx_reverse

        return result if min <= result and result <= max else 0  # @lc code=end

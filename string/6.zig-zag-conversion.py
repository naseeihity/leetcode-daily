#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows

        col = 0
        direction = 1
        for i in range(len(s)):
            rows[col] += s[i]
            col += direction
            if col == 0 or col == numRows-1:
                direction *= -1

        ans = ""

        for j in range(numRows):
            ans += rows[j]

        return ans
# @lc code=end

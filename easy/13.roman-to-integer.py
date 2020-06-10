#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0

        for i in range(len(s)-1):
            char = s[i]
            next_char = s[i+1]
            if roman[char] < roman[next_char]:
                result -= roman[char]
            else:
                result += roman[char]

        return result + roman[s[-1]]
# @lc code=end

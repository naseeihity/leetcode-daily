#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, str: str) -> int:
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, '8': 8, '9': 9, '-': '-', '+': '+'}
        s = str.strip()

        if not s or s[0] not in digits:
            return 0

        sign = 1
        start = 0
        if s[start] == '-':
            sign = -1
            start = 1
        elif s[start] == '+':
            start = 1

        ans = 0
        for c in s[start:]:
            d = digits.get(c, None)
            if d is None or d == '-' or d == '+':
                break

            if sign == -1 and ((ans > 214748364) or (ans == 214748364 and d == 9)):
                return -2147483648
            elif sign == 1 and ((ans > 214748364) or (ans == 214748364 and d > 7)):
                return 2147483647

            ans = ans * 10 + d

        return sign*ans
# @lc code=end

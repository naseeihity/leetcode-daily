#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxVal = 0
        stack = []
        stack.append(-1)

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxVal = max(maxVal, i - stack[-1])
        return maxVal
# @lc code=end

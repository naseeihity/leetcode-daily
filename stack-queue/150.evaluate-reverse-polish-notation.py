#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = int(tokens[0])
        stack = []
        operaters = ['+', '-', '*', '/']

        for c in tokens:
            if c not in operaters:
                stack.append(c)
            else:
                x1 = int(stack.pop())
                x2 = int(stack.pop())

                if c == '+':
                    ans = x1 + x2
                elif c == '-':
                    ans = x2 - x1
                elif c == '*':
                    ans = x1 * x2
                else:
                    if x2 // x1 < 0:
                        ans = math.ceil(x2 / x1)
                    else:
                        ans = x2 // x1

                stack.append(ans)

        return ans
# @lc code=end

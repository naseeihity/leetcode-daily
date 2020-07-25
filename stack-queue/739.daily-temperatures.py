#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = []

        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            if not stack:
                ans.insert(0, 0)
            else:
                ans.insert(0, stack[-1] - i)

            stack.append(i)

        return ans
# @lc code=end

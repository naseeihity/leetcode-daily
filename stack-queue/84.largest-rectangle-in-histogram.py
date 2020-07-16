#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start

# 单调栈，空间换时间
# 第 42、739、496、316、901、402、581 题


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0

        l = [0] * n
        r = [n] * n

        stack1 = []
        for i in range(n):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                r[stack1[-1]] = i
                stack1.pop()
            l[i] = stack1[-1] if stack1 else -1
            stack1.append(i)

        # stack2 = []
        # for i in range(n-1,-1,-1):
        #     while stack2 and heights[stack2[-1]] >= heights[i]:
        #         stack2.pop()
        #     r[i] = stack2[-1] if stack2 else n
        #     stack2.append(i)

        ans = max((r[i] - l[i] - 1) * heights[i]
                  for i in range(n)) if n > 0 else 0

        return ans
# @lc code=end

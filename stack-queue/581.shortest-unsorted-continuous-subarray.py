#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        m = len(nums)
        l, r = m-1, 0

        stack = []
        for i in range(m):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack2 = []
        for j in range(m-1, -1, -1):
            while stack2 and nums[stack2[-1]] < nums[j]:
                r = max(r, stack2.pop())
            stack2.append(j)

        return r - l + 1 if r - l > 0 else 0
# @lc code=end

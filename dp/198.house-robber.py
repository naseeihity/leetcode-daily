#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = n = 0
        ans = 0

        for i in range(len(nums)):
            ans = max(m, n+nums[i])
            n = m
            m = ans

        return ans

# @lc code=end

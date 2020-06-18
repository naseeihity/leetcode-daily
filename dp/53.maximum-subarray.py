#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

# TODO：分治的方法 -> 知识点：线段树


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = sub_max = nums[0]

        for i in range(1, len(nums)):
            sub_max = max(sub_max + nums[i], nums[i])
            ans = max(ans, sub_max)
        return ans
# @lc code=end

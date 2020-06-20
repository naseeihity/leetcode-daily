#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        m1, n1, ans1 = 0, 0, 0
        m2, n2, ans2 = 0, 0, 0
        for i in range(len(nums)-1):
            ans1 = max(m1, n1+nums[i])
            n1 = m1
            m1 = ans1

        for j in range(1, len(nums)):
            ans2 = max(m2, n2+nums[j])
            n2 = m2
            m2 = ans2

        return max(ans1, ans2)
# @lc code=end

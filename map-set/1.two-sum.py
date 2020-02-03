#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for i, x in enumerate(nums):
            y = target - x
            if y not in num_map:
                num_map[x] = i
            else:
                return [num_map[y], i]

# @lc code=end

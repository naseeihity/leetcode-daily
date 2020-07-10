#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        reach = 0
        step = 0
        farest = 0

        for i in range(size-1):
            if reach >= i:
                reach = max(reach, i+nums[i])

                if i == farest:
                    farest = reach
                    step += 1

        return step  # @lc code=end

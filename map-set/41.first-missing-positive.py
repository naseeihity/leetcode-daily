#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        # the answer must equal to or smaller than len(nums)
        max = len(nums)

        for i in range(max):
            if nums[i] < 0 or nums[i] >= max:
                nums[i] = 0
        # use the index as the hash to record the frequency of each number
        for i in range(max):
            nums[nums[i] % max] += max

        for i in range(1, max):
            if nums[i] // max == 0:
                return i

        return max
# @lc code=end

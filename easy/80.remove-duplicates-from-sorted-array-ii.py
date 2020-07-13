#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        a, b = 0, 2

        for i in range(2, n):
            if nums[i] != nums[b-1] or nums[i] != nums[b-2]:
                nums[b] = nums[i]
                b += 1

        return b
# @lc code=end

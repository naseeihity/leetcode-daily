#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
                l += 1
            elif nums[l] <= nums[mid] <= nums[r]:
                r -= 1

        return nums[l]
# @lc code=end

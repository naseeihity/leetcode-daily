#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def findBound(self, nums, target, left):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                if left:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if left:
            return l if l < len(nums) and nums[l] == target else -1
        else:
            return r if r >= 0 and nums[r] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = self.findBound(nums, target, True)
        right = self.findBound(nums, target, False)

        return [left, right]
# @lc code=end

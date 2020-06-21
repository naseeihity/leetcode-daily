#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[-1]:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
# @lc code=end

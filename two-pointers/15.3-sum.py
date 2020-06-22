#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                sum = num + nums[left] + nums[right]
                if sum < 0:
                    left = left + 1
                elif sum > 0:
                    right = right - 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1

        return ans
# @lc code=end

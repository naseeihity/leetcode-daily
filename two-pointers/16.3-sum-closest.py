#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start


class Solution:
    # Two pointers
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        distance = float('inf')
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if abs(target - sum) < abs(distance):
                    distance = target - sum

                if sum < target:
                    l += 1
                else:
                    r -= 1

                if distance == 0:
                    break

        return target - distance
# @lc code=end

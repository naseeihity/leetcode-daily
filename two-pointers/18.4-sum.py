#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start


class Solution:
    # two pointers
    def twoSum(self, nums, target):
        res = []
        l, r = 0, len(nums)-1

        while l < r:
            sum = nums[l] + nums[r]
            if sum < target or (l > 0 and nums[l] == nums[l-1]):
                l += 1
            elif sum > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1

        return res
    # hash-set

    def twoSum(self, nums, target):
        res = []
        s = set()

        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
                s.add(nums[i])

        return res

    def kSum(self, nums, target, k):
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return []
        if k == 2:
            return self.twoSum(nums, target)

        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for _, set in enumerate(self.kSum(nums[i+1:], target-nums[i], k-1)):
                    res.append([nums[i]] + set)
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
# @lc code=end

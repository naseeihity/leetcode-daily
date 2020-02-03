#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i, item in enumerate(nums[:-2]):
            if i >= 1 and item == nums[i - 1]:
                continue
            d = {}

            for x in nums[i+1:]:
                if x not in d:
                    d[-item-x] = 1
                else:
                    ans.add((item, -item-x, x))
        return map(list, ans)
# @lc code=end

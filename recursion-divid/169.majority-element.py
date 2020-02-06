import collections
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (55.02%)
# Likes:    2200
# Dislikes: 187
# Total Accepted:    470K
# Total Submissions: 854.3K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start


class Solution:
    def majorityElement(self, nums):
        # return collections.Counter(nums).most_common(1)[0][0]
        def divid(l, r):
            if l == r:
                return nums[l]

            mid = (r - l) // 2 + l
            left = divid(l, mid)
            right = divid(mid + 1, r)

            if (left == right):
                return left

            left_count = sum(1 for i in range(l, r+1) if nums[i] == left)
            right_count = sum(1 for i in range(l, r+1) if nums[i] == right)

            return left if left_count > right_count else right
        return divid(l=0, r=len(nums) - 1)
# @lc code=end

# day3

from typing import List
import collections

# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (54.13%)
# Likes:    538
# Dislikes: 602
# Total Accepted:    429.7K
# Total Submissions: 793.7K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set 去重
        # numsSet = set(nums)
        # return len(numsSet) != len(nums)

        # hash table
        table = {}

        for num in nums:
            if num not in table:
                table[num] = num
            else:
                return True

        return False

# @lc code=end
# 可以归类为去重问题

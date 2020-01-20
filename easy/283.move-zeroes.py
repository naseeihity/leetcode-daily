# day 2

from typing import List
#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.74%)
# Likes:    2633
# Dislikes: 94
# Total Accepted:    572.9K
# Total Submissions: 1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#

# @lc code=start

# complex
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = 0
#         finish = False
#         for i in range(len(nums) - 1):
#             k = max(i + 1, k)
#             if nums[i] != 0:
#                 continue
#             else:
#                 for j, num in enumerate(nums[k:]):
#                     if num == 0:
#                         finish = True
#                         continue
#                     else:
#                         finish = False
#                         nums[i], nums[k + j] = nums[k + j], nums[i]
#                         k = j + 1
#                         break
#                 if finish:
#                     break


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
# @lc code=end

# in-place modify

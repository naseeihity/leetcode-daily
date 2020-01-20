# day 1

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.19%)
# Likes:    3133
# Dislikes: 123
# Total Accepted:    578K
# Total Submissions: 929.5K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start

# 哈希表法思路
# 第一次 table[item] = 1
# 第二次 table.pop(item)
# 剩到最后的pop出来就是结果

# code
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         hash_table = {}
#         for i in nums:
#             try:
#                 hash_table.pop(i)
#             except:
#                 hash_table[i] = 1
#         return hash_table.popitem()[0]

# 利用 按位异或的法则
# a ^ 0 = a
# a ^ a = 0 ==> 推得
# a ^ b ^ a = b


class Solution:
    def singleNumber(self, nums):
        for i in range(len(nums)-1):
            nums[i+1] ^= nums[i]
        return nums[-1]
# @lc code=end

# 按位 xor 的方法，解决一些存在成对相同数字的问题

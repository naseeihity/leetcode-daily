from typing import List

#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (64.86%)
# Likes:    964
# Dislikes: 597
# Total Accepted:    548.8K
# Total Submissions: 846.2K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
#
# Example 1:
#
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
#
#
# Example 2:
#
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
#
#

# O(N) space complexity to keep recursion stack
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         def helper(l: int, r: int):
#             if (l < r):
#                 s[l], s[r] = s[r], s[l]
#                 helper(l + 1, r - 1)

#         helper(0, len(s) - 1)

# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# @lc code=end

# 理解O(1)的空间复杂度，理解递归所产生的额外的空间复杂度
# day1

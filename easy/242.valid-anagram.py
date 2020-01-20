# Day 2
import collections
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (54.38%)
# Likes:    976
# Dislikes: 124
# Total Accepted:    436K
# Total Submissions: 801.8K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#

# @lc code=start

# my solution
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ans = True
#         for char in s:
#             try:
#                 t = t[0:t.index(char)] + t[t.index(char)+1:]
#             except:
#                 ans = False
#                 break

#         if len(t) != 0:
#             ans = False
#         return ans

# Approch 1
# sort, sort make the two str same

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if (len(s) != len(t)):
#             return False

#         _s = sorted(s)
#         _t = sorted(t)
#         return _s == _t


# Approch 2
# Hash table: collections.Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        return all([cs[c] == ct[c] for c in cs]) and len(cs) == len(ct)

# @lc code=end


# 对于一些字符串比较的问题考虑两种方法
# 1. 排序后比较
# 2. hash table

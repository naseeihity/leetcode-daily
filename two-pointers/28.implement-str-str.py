#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        len_h = len(haystack)
        len_n = len(needle)
        point = 0

        while point < len_h - len_n + 1:
            while point < len_h - len_n + 1 and haystack[point] != needle[0]:
                point += 1

            match = cur_point = 0
            while point < len_h and cur_point < len_n and haystack[point] == needle[cur_point]:
                point += 1
                cur_point += 1
                match += 1

            if match == len_n:
                return point - match

            point = point - match + 1

        return -1
# @lc code=end

#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            while prefix not in strs[i] or strs[i].index(prefix) != 0:
                prefix = prefix[:len(prefix)-1]
                if not prefix:
                    return ""

        return prefix
# @lc code=end

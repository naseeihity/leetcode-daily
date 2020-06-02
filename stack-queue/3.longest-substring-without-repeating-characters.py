from collections import defaultdict
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(lambda: 0)
        left, right, maxLen = 0, 0, 0

        while right < len(s):
            item = s[right]
            right += 1
            window[item] += 1

            while window[item] > 1:
                item_out = s[left]
                left += 1
                window[item_out] -= 1

            maxLen = max(maxLen, right - left)

        return maxLen
# @lc code=end

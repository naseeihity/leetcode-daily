from collections import defaultdict
#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = float('inf')
        start = 0
        window, target = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for c in t:
            target[c] += 1

        left, right = 0, 0
        # number of valid characters in window
        valid = 0

        while right < len(s):
            item = s[right]
            right += 1

            if item in target:
                window[item] += 1
                if window[item] == target[item]:
                    valid += 1

            while valid == len(target):
                if right - left < length:
                    start = left
                    length = right - left

                out_item = s[left]
                left += 1

                if out_item in target:
                    if window[out_item] == target[out_item]:
                        valid -= 1
                    window[out_item] -= 1

        ans = s[start:start+length] if length < float('inf') else ''
        return ans
# @lc code=end

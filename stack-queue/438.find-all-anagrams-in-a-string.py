from collections import defaultdict
#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, target = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for c in p:
            target[c] += 1
        left, right = 0, 0
        valid = 0
        ans = []

        while right < len(s):
            item = s[right]
            right += 1

            if item in target:
                window[item] += 1
                if window[item] == target[item]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(target):
                    ans.append(left)

                item_out = s[left]
                left += 1

                if item_out in target:
                    if window[item_out] == target[item_out]:
                        valid -= 1
                    window[item_out] -= 1

        return ans
# @lc code=end

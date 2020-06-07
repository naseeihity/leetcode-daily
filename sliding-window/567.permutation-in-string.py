from collections import defaultdict
#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, target = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for c in s1:
            target[c] += 1
        left, right = 0, 0
        valid = 0

        while right < len(s2):
            item = s2[right]
            right += 1

            if item in target:
                window[item] += 1
                if window[item] == target[item]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(target):
                    return True

                item_out = s2[left]
                left += 1

                if item_out in target:
                    if window[item_out] == target[item_out]:
                        valid -= 1
                    window[item_out] -= 1

        return False


# @lc code=end

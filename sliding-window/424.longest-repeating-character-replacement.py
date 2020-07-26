#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = collections.defaultdict(lambda: 0)
        l, r = 0, 0
        m = 0
        ans = 0

        while r < len(s):
            cur = s[r]
            window[cur] += 1
            m = max(m, window[cur])

            while r - l + 1 - m > k:
                out = s[l]
                l += 1
                window[out] -= 1

            ans = max(ans, r-l+1)
            r += 1

        return ans

# @lc code=end

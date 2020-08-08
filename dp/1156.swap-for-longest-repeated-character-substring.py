#
# @lc app=leetcode id=1156 lang=python3
#
# [1156] Swap For Longest Repeated Character Substring
#

# @lc code=start


class Solution:
    def count(self, c, text):
        ans = 0
        f, g = 0, 0

        for i in range(len(text)):
            if c == text[i]:
                f += 1
                g += 1
            else:
                f = g+1
                g = 0

            ans = max(ans, f, g)
        return ans

    def maxRepOpt1(self, text: str) -> int:
        if not text:
            return 0

        d = collections.Counter(text)

        ans = 0
        for char in d.keys():
            ans = max(ans, min(self.count(char, text), d[char]))

        return ans
# @lc code=end

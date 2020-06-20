#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memorize = {}

        def wordBreak(s):
            if s in memorize:
                return memorize[s]
            ans = []
            if s in wordDict:
                ans.append(s)

            for i in range(1, len(s)):
                right = s[i:]
                if not right in wordDict:
                    continue
                ans += [w + " " + right for w in wordBreak(s[0:i])]

            memorize[s] = ans
            return memorize[s]
        return wordBreak(s)
# @lc code=end

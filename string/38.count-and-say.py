#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        def say(self, ans):
        _ans = ""
        l, r = 0, len(ans)
        for i in range(1, r+1):
            if i == r or ans[l] != ans[i]:
                count = i - l
                _ans += str(count)
                _ans += ans[l]
                l = i
        return _ans

    def countAndSay(self, n: int) -> str:
        ans = "1"

        for i in range(1, n):
            ans = self.say(ans)

        return ans
# @lc code=end

#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start

# 回溯法


class Solution:
    def valid(self, s):
        return int(s) <= 255 if s[0] != "0" else len(s) == 1

    def dfs(self, s, track, num):
        if num == 4:
            if len(s) == 0:
                self.result.append('.'.join(track))
            return

        for i in range(1, 4):
            if i <= len(s):
                sub_s = s[:i]
                if self.valid(sub_s):
                    track.append(sub_s)
                    new_s = s[i:]
                    self.dfs(new_s, track, num+1)
                    track.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        self.result = []
        self.dfs(s, [], 0)

        return self.result
# @lc code=end

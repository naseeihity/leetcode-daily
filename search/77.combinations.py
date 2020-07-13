#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
     def dfs(self, target, start, ans, n, k):
        if len(target) == k:
            ans.append(target)
            return

        for i in range(start, n):
            self.dfs(target+[i+1], i+1, ans, n, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs([], 0, ans, n, k)
        return ans   
# @lc code=end


#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def dfs(self, start, size, cur, ans, nums):
        if size == len(cur):
            ans.append(cur)
            return

        for i in range(start, len(nums)):
            self.dfs(i+1, size, cur + [nums[i]], ans, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        for i in range(len(nums)+1):
            self.dfs(0, i, [], self.ans, nums)

        return self.ans
# @lc code=end

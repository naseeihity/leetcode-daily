#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def dfs(self, nums, depth, size, used, cur, ans):
        if depth == size:
            ans.append(cur)
            return

        for i in range(size):
            if used[i]:
                continue
            used[i] = True
            self.dfs(nums, depth+1, size, used, cur+[nums[i]], ans)
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        ans = []
        size = len(nums)
        used = [False for _ in range(size)]
        cur = []

        self.dfs(nums, 0, size, used, cur, ans)

        return ans
# @lc code=end

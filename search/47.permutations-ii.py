#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
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
            # not used[i-1]刚刚被撤销选择的那个数, 同一深度不能重复选择
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            self.dfs(nums, depth+1, size, used, cur+[nums[i]], ans)
            used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        ans = []
        size = len(nums)
        used = [False for _ in range(size)]
        cur = []
        nums.sort()

        self.dfs(nums, 0, size, used, cur, ans)

        return ans
# @lc code=end

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
# 0-1背包问题


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        N = len(nums)

        half, left = divmod(total, 2)
        if left != 0:
            return False

        dp = [False]*(half+1)
        dp[0] = True

        for i in range(N):
            for j in range(half, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[half]  # @lc code=end

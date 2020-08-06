#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
# 将回溯问题转为dp
# Sum(part) = (total + target)//2 的方案个数


class Solution:
    def countSubset(self, nums, target):
        n = len(nums)
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

        # 把i个物品放入容量为j的背包的方法数
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)

        if total < S or (total + S) % 2 != 0:
            return 0

        return self.countSubset(nums, (total+S) // 2)
# @lc code=end

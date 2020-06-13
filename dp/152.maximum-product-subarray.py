#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][0], dp[0][1], ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i+1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])

            ans = max(ans, dp[x][0])

        return ans
# @lc code=end

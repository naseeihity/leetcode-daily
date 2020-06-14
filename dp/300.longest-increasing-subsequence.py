#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

import bisect


class Solution:
    # 二分查找 O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = []
        for i in range(len(nums)):
            smallest_index = bisect.bisect_left(ans, nums[i])
            if smallest_index == len(ans):
                ans.append(nums[i])
            else:
                ans[smallest_index] = nums[i]

        return len(ans)
    # dp O(n^2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     size = len(nums)
    #     dp = [1 for _ in range(size)]

    #     for i in range(1, size):
    #         for j in range(0, i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return max(dp)
# @lc code=end

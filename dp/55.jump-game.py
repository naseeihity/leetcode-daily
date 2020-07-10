#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start


class Solution:
    # dp
    # def canJump(self, nums: List[int]) -> bool:
    #     size = len(nums)
    #     if size <= 1:
    #         return True

    #     dp = [False for _ in range(size)]
    #     dp[0] = True

    #     for i in range(1, size):
    #         for j in range(i-1, -1, -1):
    #             if dp[j] and j + nums[j] >= i:
    #                 dp[i] = True
    #                 break

    #     return dp[size-1]

    # greedy
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        reach = 0

        for i in range(size):
            if i <= reach:
                reach = max(reach, i+nums[i])
                if reach >= size - 1:
                    return True

        return False
# @lc code=end

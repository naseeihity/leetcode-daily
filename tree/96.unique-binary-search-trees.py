#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
# 动态规划问题


class Solution:
    def numTrees(self, n: int) -> int:
        a = [0] * (n+1)
        a[0] = a[1] = 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                a[i] += a[k-1] * a[i-k]

        return a[n]
# @lc code=end

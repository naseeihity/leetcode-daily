#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        k = len(triangle)
        ans = triangle[-1]

        for i in range(k-2, -1, -1):
            for j in range(len(triangle[i])):
                ans[j] = min(ans[j], ans[j+1]) + triangle[i][j]

        return ans[0]
# @lc code=end

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        size = len(height)
        l = [0 for _ in range(size)]
        r = [0 for _ in range(size)]
        ans = 0
        l[0] = height[0]
        r[size-1] = height[size-1]

        for i in range(1, size):
            l[i] = max(l[i-1], height[i])

        for j in range(size-2, -1, -1):
            r[j] = max(r[j+1], height[j])

        for k in range(size):
            ans = ans + min(l[k], r[k])-height[k]

        return ans
# @lc code=end


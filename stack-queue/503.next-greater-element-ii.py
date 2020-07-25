#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1] * l
        nums2 = nums + nums

        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()

            res[i % l] = -1 if not stack else nums2[stack[-1]]

            stack.append(i % l)

        return res
# @lc code=end

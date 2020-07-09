#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A)

        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] < A[mid+1]:
                l = mid + 1
            else:
                r = mid - 1

        return l
# @lc code=end

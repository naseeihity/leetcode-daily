#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#

# @lc code=start


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        ans = 0

        for i in range(1, len(A)-1):
            l, r = i, i

            if A[i] <= A[i-1] or A[i] <= A[i+1]:
                continue

            while l > 0 and A[l-1] < A[l]:
                l -= 1

            while r < len(A)-1 and A[r+1] < A[r]:
                r += 1

            ans = max(ans, r-l+1)

        return ans if ans >= 3 else 0
# @lc code=end

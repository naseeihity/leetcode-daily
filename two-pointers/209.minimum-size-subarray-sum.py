#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start


class Solution:
    # binary search O(nlogn)
    # 因为是找连续的序列，所以又一个单调增长的子序列和
    def binarySearch(self, l, r, target, arr):
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]

        for j in range(1, n+1):
            total = s + sums[j-1]
            right = self.binarySearch(j, n, total, sums)

            if right != n+1:
                ans = min(ans, right-j+1)

        return ans if ans != n+1 else 0

    # sliding window / two pointers
    # O(n)
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     n = len(nums)
    #     ans = n+1
    #     l, _sum = 0, 0

    #     for i in range(n):
    #         _sum += nums[i]

    #         while _sum >= s:
    #             ans = min(ans, i+1-l)
    #             _sum -= nums[l]
    #             l += 1

    #     return ans if ans != n+1 else 0
# @lc code=end

#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if (n1 > n2):
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        l, r = 0, n1 - 1

        while l <= r:
            mid = l + (r-l) // 2
            if nums1[mid] < nums2[k-mid-1]:
                l = mid + 1
            else:
                r = mid - 1

        m1 = l
        m2 = k - l

        num1 = nums1[m1-1] if m1 > 0 else float('-inf')
        num2 = nums2[m2-1] if m2 > 0 else float('-inf')

        median1 = max(num1, num2)

        if (n1+n2) % 2 == 1:
            return median1

        num3 = nums1[m1] if m1 < n1 else float('inf')
        num4 = nums2[m2] if m2 < n2 else float('inf')

        median2 = min(num3, num4)

        return (median1+median2)/2
# @lc code=end

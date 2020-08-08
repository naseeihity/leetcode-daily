#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
#DP + Greedy


class Solution:
    def maxK(self, nums, k):
        ans = [0] * k
        n = len(nums)
        j = 0

        for i in range(n):

            while j > 0 and nums[i] > ans[j-1] and n - i > k - j:
                j -= 1

            if j < k:
                ans[j] = nums[i]
                j += 1

        return ans

    def maxConcat(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        ans = [0]*(n1+n2)
        s1, s2, index = 0, 0, 0

        while s1 != n1 or s2 != n2:
            if nums1[s1:] > nums2[s2:]:
                ans[index] = nums1[s1]
                s1 += 1
            else:
                ans[index] = nums2[s2]
                s2 += 1

            index += 1

        return ans

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []

        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(max(0, k-n2), min(k, n1)+1):
            temp = self.maxConcat(self.maxK(nums1, i), self.maxK(nums2, k-i))
            if ans < temp:
                ans = temp

        return ans
# @lc code=end

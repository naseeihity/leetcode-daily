#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
# Insertion Sorting


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 0:
            return []
        ans = []
        window = sorted(nums[0:k])

        for i in range(k, len(nums)+1):
            ans.append((window[k//2]+window[(k-1)//2])/2)

            if i == len(nums):
                break

            idx = bisect.bisect_left(window, nums[i-k])
            window.pop(idx)
            bisect.insort_left(window, nums[i])

        return ans
# @lc code=end

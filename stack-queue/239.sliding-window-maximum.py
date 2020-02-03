#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        window, ans = [], []
        for i, item in enumerate(nums):
            if i >= k and i - k >= window[0]:
                window.pop(0)
            while window and nums[window[-1]] <= item:
                window.pop()
            window.append(i)
            if i >= k - 1:
                ans.append(nums[window[0]])
        return ans
# @lc code=end

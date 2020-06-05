#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = heapq.nlargest(k, nums + [float('-inf')])
        heapq.heapify(self.nums)

    def add(self, val):

        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
        heapq.heappushpop(self.nums, val)
        return self.nums[0]
        # @lc code=end

#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
# 堆排序


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def buildMaxHeap(a, size):
            for i in range(size//2, -1, -1):
                maxHeapify(a, i, size)

        def maxHeapify(a, i, size):
            l, r, largest = i * 2 + 1, i * 2 + 2, i
            if l < size and a[l] > a[largest]:
                largest = l
            if r < size and a[r] > a[largest]:
                largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                maxHeapify(a, largest, size)

        size = len(nums)
        buildMaxHeap(nums, size)
        # 如果k等于size，最终的nums就是从小到大排列的
        for i in range(len(nums)-1, len(nums)-k, -1):
            # 删除最大元素（移到数组空处），将末尾元素放到头部，然后通过sink重新构建堆
            nums[0], nums[i] = nums[i], nums[0]
            size -= 1
            maxHeapify(nums, 0, size)

        return nums[0]
# @lc code=end

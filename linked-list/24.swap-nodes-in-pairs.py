# type: ignore
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            left = pre.next
            right = left.next
            pre.next, left.next, right.next = right, right.next, left
            pre = left
        return self.next
    # @lc code=end

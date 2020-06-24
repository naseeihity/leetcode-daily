#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = PriorityQueue()

        i = 0
        for l in lists:
            if l:
                q.put((l.val, i, l))
                i += 1

        while not q.empty():
            val, _id, node = q.get()
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put((node.val, i, node))
                i += 1

        return head.next

    # Divide And Conquer
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     dummy = cur = ListNode(0)

    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next

    #     cur.next = l1 or l2
    #     return dummy.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     n = len(lists)
    #     tmp = 1

    #     while tmp < n:
    #         for i in range(0, n-tmp, tmp*2):
    #             lists[i] = self.mergeTwoLists(lists[i], lists[i+tmp])
    #         tmp *= 2

    #     return lists[0] if n > 0 else None
    # @lc code=end

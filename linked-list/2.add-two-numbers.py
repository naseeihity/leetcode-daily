#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        p, q = l1, l2

        k = 0

        while p or q:
            x1 = p.val if p else 0
            x2 = q.val if q else 0

            sum = x1 + x2 + k

            k = sum // 10
            sum = sum % 10

            cur.next = ListNode(sum)
            cur = cur.next

            if p:
                p = p.next
            if q:
                q = q.next

        if k > 0:
            cur.next = ListNode(k)

        return dummy.next
# @lc code=end

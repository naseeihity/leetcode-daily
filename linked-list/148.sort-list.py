#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Top-down merge sort
    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        cur.next = left or right
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return self.merge(self.sortList(head), self.sortList(mid))


# class Solution:
#     def split(self, head, n):
#         while n-1 and head:
#             n -= 1
#             head = head.next

#         rest = head.next if head else None
#         if head:
#             head.next = None

#         return rest

#     def merge(self, left, right):
#         dummy = ListNode(0)
#         cur = dummy

#         while left and right:
#             if left.val <= right.val:
#                 cur.next = left
#                 left = left.next
#             else:
#                 cur.next = right
#                 right = right.next

#             cur = cur.next

#         cur.next = left or right
#         while cur.next:
#             cur = cur.next

#         return dummy.next, cur

#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head

#         cur = head
#         length = 0
#         while cur:
#             cur = cur.next
#             length += 1

#         dummy = ListNode(0)
#         dummy.next = head
#         step = 1

#         while step < length:
#             cur = dummy.next
#             tail = dummy

#             while cur:
#                 l = cur
#                 r = self.split(l, step)
#                 cur = self.split(r, step)
#                 tail.next, tail = self.merge(l, r)

#             step <<= 1

#         return dummy.next

# @lc code=end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m = m - 1
            n = n - 1

        sub_tail = cur
        fix_head = prev

        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n = n - 1

        if fix_head:
            fix_head.next = prev
        else:
            head = prev

        sub_tail.next = cur
        return head

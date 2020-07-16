#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        cur = head
        prev = dummy

        while cur and cur.next:
            if prev.next.val != cur.next.val:
                prev = prev.next
                cur = cur.next
            else:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next

                prev.next = cur.next
                cur = cur.next

        return dummy.next
# @lc code=end

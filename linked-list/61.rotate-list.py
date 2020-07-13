#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head
        # 第 (n - k % n - 1) 个节点为新的尾部

        new_tail = head
        for _ in range(n-k % n-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
# @lc code=end

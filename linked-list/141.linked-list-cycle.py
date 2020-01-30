# type: ignore
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# quick and fast
# avoid use more space

# class Solution:
#     def hasCycle(self, head):
#         fast = slow = head
#         while slow and fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow in fast:
#                 return True
#         return False


class Solution:
    def hasCycle(self, head):
        nodes = set()
        cur = head
        while cur:
            if cur in nodes:
                return True
            else:
                nodes.add(cur)
                cur = cur.next

        return False
        # @lc code=end

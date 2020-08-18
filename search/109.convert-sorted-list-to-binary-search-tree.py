#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getListCenter(self, head):
        dummy = None
        slow, fast = head, head
        while fast and fast.next:
            dummy = slow
            slow = slow.next
            fast = fast.next.next

        if dummy:
            dummy.next = None
        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        mid = self.getListCenter(head)

        root = TreeNode(mid.val)

        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
# @lc code=end

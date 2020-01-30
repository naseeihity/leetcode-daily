#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        linkHead = groupHead = ListNode(0)
        linkHead.next = left = right = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            if count == k:
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                groupHead.next, groupHead, left = pre, left, right
            else:
                return linkHead.next
        # @lc code=end

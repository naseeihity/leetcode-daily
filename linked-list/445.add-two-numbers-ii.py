#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []

        while l1 or l2:
            if l1:
                stack1.append(l1)
                l1 = l1.next
            if l2:
                stack2.append(l2)
                l2 = l2.next

        k = 0
        ans = None

        while stack1 or stack2 or k:
            num1 = stack1.pop().val if stack1 else 0
            num2 = stack2.pop().val if stack2 else 0

            _sum = num1 + num2 + k

            k, num = divmod(_sum, 10)
            node = ListNode(num)
            node.next = ans
            ans = node

        return ans
# @lc code=end

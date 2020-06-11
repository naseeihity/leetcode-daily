#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # DFS
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        next_node = root.next
        while next_node:
            if next_node.left:
                next_node = next_node.left
                break
            if next_node.right:
                next_node = next_node.right
                break

            next_node = next_node.next

        if root.right:
            root.right.next = next_node
        if root.left:
            root.left.next = root.right if root.right else next_node

        if root.right:
            self.connect(root.right)
        if root.left:
            self.connect(root.left)

        return root
    # BFS 同116

# @lc code=end

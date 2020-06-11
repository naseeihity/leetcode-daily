#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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
        if not root or not root.left:
            return root
        root.left.next = root.right

        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

    # BFS
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return root

    #     queue = []
    #     queue.append(root)

    #     while queue:
    #         size = len(queue)
    #         for i in range(size):
    #             cur = queue.pop(0)
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)

    #             if i < size - 1:
    #                 next_node = queue[0]
    #                 cur.next = next_node

    #     return root
# @lc code=end

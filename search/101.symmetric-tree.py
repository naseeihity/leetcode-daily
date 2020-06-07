#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(self, l1: TreeNode, l2: TreeNode):
        if not l1 and not l2:
            return True
        if not l1 or not l2:
            return False

        return l1.val == l2.val and self.isMirror(l1.right, l2.left) and self.isMirror(l1.left, l2.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    # BFS
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     queue = []
    #     if not root:
    #         return True
    #     queue.append(root.left)
    #     queue.append(root.right)

    #     while queue:
    #         left = queue.pop()
    #         right = queue.pop()
    #         if not left and not right:
    #             continue
    #         if not left or not right or left.val != right.val:
    #             return False

    #         queue.append(left.left)
    #         queue.append(right.right)
    #         queue.append(left.right)
    #         queue.append(right.left)

    #     return True
# @lc code=end

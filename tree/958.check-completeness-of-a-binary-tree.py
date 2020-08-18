#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = []
        queue.append((root, 1))
        i = 0
        while i < len(queue):
            node, n = queue[i]
            i += 1

            if node.left:
                queue.append((node.left, 2*n))
            if node.right:
                queue.append((node.right, 2*n+1))

        return queue[-1][1] == len(queue)

# @lc code=end

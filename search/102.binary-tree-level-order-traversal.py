import collections
#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return []
#         self.result = []
#         self._dfs(root, 0)
#         return self.result

#     def _dfs(self, node, level):
#         if not node:
#             return

#         if len(self.result) < level + 1:
#             self.result.append([])

#         self.result[level].append(node.val)

#         self._dfs(node.left, level + 1)
#         self._dfs(node.right, level + 1)

# bfs
class Solution:
    def levelOrder(self, root):
        queue = []
        arr = []
        if not root:
            return []
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            arr.append(level)

        return arr
# @lc code=end

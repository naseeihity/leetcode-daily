#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, node, sum):
        left = 0
        right = 0
        if not node.left and not node.right:
            return sum*10 + node.val

        if node.left:
            left = self.dfs(node.left, sum*10+node.val)
        if node.right:
            right = self.dfs(node.right, sum*10+node.val)

        return left + right

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, 0)
# @lc code=end

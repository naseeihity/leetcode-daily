#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        left, right = False, False
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        if root.left:
            left = self.hasPathSum(root.left, sum - root.val)

        if root.right:
            right = self.hasPathSum(root.right, sum - root.val)

        return left or right
# @lc code=end

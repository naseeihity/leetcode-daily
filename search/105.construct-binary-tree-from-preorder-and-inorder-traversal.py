#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            idx = inorder.index(preorder.pop(0))

            rootNode = TreeNode(inorder[idx])
            rootNode.left = self.buildTree(preorder, inorder[:idx])
            rootNode.right = self.buildTree(preorder, inorder[idx+1:])

            return rootNode
# @lc code=end

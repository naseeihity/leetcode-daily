#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, first, last):
        tree = []
        for root in range(first, last+1):
            for left in self.helper(first, root-1):
                for right in self.helper(root+1, last):
                    tree.append(TreeNode(root, left, right))
        return tree or [None]

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n) if n else []
# @lc code=end

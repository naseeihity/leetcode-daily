#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历
# class Solution:
#     def isValidBST(self, root):
#         inOderList = self.inOder(root)
#         return inOderList == list(sorted(set(inOderList)))

#     def inOder(self, root):
#         if root is None:
#             return []
#         return self.inOder(root.left) + [root.val] + self.inOder(root.right)、


# recursion
class Solution:
    def isValidBST(self, root):
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, root, min, max):
        if root is None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False

        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)

# @lc code=end

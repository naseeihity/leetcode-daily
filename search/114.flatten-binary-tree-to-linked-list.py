#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.pre = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.pre
        root.left = None
        self.pre = root

    # directly
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            # 如果没有左子树，则root到下一个节点
            if not root.left:
                root = root.right
            else:
                pre = root.left
                # 找到左子树的最右侧的节点
                while pre.right:
                    pre = pre.right
                # 把右子树接到左子树的最右侧的节点
                pre.right = root.right
                # 把左子树接到根结点的右侧
                root.right = root.left
                # 左子树清空
                root.left = None
                # 下一个节点
                root = root.right

# @lc code=end

#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # Morris
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pred = predecessor = None

        while root:
            if not root.left:
                if pred and pred.val > root.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and pred.val > root.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right

        x.val, y.val = y.val, x.val
    # using stack
    # def recoverTree(self, root: TreeNode) -> None:
    #     stack = []
    #     x = y = pred = None

    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()

    #         if pred and pred.val > root.val:
    #             y = root
    #             if not x:
    #                 x = pred
    #             else:
    #                 break

    #         pred = root
    #         root = root.right

    #     x.val, y.val = y.val, x.val
    # general idea
    # space O(n)
    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     def inorder(root):
    #         return inorder(root.left) + [root.val] + inorder(root.right) if root else []

    #     nums = inorder(root)

    #     def find_swap(nums):
    #         x = y = -1
    #         for i in range(len(nums)-1):
    #             if nums[i] > nums[i+1]:
    #                 y = nums[i+1]
    #                 if x == -1:
    #                     x = nums[i]
    #                 else:
    #                     break
    #         return x, y
    #     x, y = find_swap(nums)

    #     def recover(root, count):
    #         if root:
    #             if root.val == x or root.val == y:
    #                 root.val = y if root.val == x else x
    #                 count -= 1
    #                 if count == 0:
    #                     return

    #             recover(root.left, count)
    #             recover(root.right, count)

    #     recover(root, 2)
    # @lc code=end

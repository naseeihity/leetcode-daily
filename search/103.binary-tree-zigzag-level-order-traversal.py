#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        arr = []
        if not root:
            return []
        queue.append(root)
        inverse = True

        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                cur = queue.pop(size-i-1)
                level.append(cur.val)

                if inverse:
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                else:
                    if cur.right:
                        queue.append(cur.right)
                    if cur.left:
                        queue.append(cur.left)

            arr.append(level)
            inverse = not inverse

        return arr
# @lc code=end

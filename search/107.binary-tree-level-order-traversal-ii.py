#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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

            arr.insert(0, level)

        return arr
# @lc code=end

#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # iteratively
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = []
        ans = []

        queue.append(root)

        while queue:
            cur = queue.pop()
            ans.append(cur.val)

            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)

        return ans
    # Recursive
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# @lc code=end

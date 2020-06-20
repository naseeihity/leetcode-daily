#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = []
        ans = []

        cur = root

        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left

            cur = q.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans
    # Recursive
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
# @lc code=end

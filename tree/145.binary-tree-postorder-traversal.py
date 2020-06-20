#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = []
        a = []

        q.append((root, False))

        while q:
            cur, status = q.pop()
            if status:
                a.append(cur.val)
            else:
                q.append((cur, True))
                if cur.right:
                    q.append((cur.right, False))
                if cur.left:
                    q.append((cur.left, False))

        return a

    # recursive
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
# @lc code=end

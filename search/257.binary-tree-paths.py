#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []

        def dfs(root, path):
            if root and not root.left and not root.right:
                ans.append(path)
                return

            if root.left:
                dfs(root.left, path+"->"+str(root.left.val))
            if root.right:
                dfs(root.right, path+"->"+str(root.right.val))

        dfs(root, str(root.val))

        return ans
# @lc code=end

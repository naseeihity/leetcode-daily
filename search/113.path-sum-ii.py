#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root, sum, path):
        if not root:
            return
        if root.val == sum and not root.left and not root.right:
            path += [root.val]
            self.allPath.append(path)

        self.dfs(root.left, sum - root.val, path + [root.val])
        self.dfs(root.right, sum - root.val, path + [root.val])

    def pathSum(self, root: TreeNode, sum: int,) -> List[List[int]]:

        self.allPath = []
        self.dfs(root, sum, [])

        return self.allPath
# @lc code=end

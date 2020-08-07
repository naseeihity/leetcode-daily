#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dp(self, root):
        if not root:
            return [0, 0]

        left = self.dp(root.left)
        right = self.dp(root.right)

        do = root.val + left[0] + right[0]
        notdo = max(left[0], left[1]) + max(right[0], right[1])

        return [notdo, do]

    def rob(self, root: TreeNode) -> int:
        ans = self.dp(root)

        return max(ans)
# @lc code=end

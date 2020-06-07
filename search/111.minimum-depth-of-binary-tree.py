#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        queue = []
        if not root:
            return 0

        queue.append(root)
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return depth

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth

    # def minDepth(self, root):
    #     if not root:
    #         return 0

    #     left = self.minDepth(root.left)
    #     right = self.minDepth(root.right)

    #     if (left == 0 or right == 0):
    #         return left + right + 1
    #     else:
    #         return min(left, right) + 1
# @lc code=end

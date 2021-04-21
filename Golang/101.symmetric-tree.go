/*
 * @lc app=leetcode id=101 lang=golang
 *
 * [101] Symmetric Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    return isMirror(root, root)
}

func isMirror(l1 *TreeNode, l2 *TreeNode) bool {
	
	if l1 == nil && l2 == nil {
		return true
	}

	if l1 == nil || l2 == nil {
		return false
	}

	return l1.Val == l2.Val && isMirror(l1.Left, l2.Right) && isMirror(l1.Right, l2.Left)
}
// @lc code=end


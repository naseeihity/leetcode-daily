/*
 * @lc app=leetcode id=872 lang=golang
 *
 * [872] Leaf-Similar Trees
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
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    arr := []int{}

		var dfs func(*TreeNode)
		dfs = func (node *TreeNode)  {
			if node == nil {
				return
			}

			if node.Left == nil && node.Right == nil {
				arr = append(arr, node.Val)
				return
			}

			dfs(node.Left)
			dfs(node.Right)
		}

		dfs(root1)
		arr1 := []int{}
		arr1 = append(arr1, arr...)

		arr = []int{}
		dfs(root2)
		arr2 := []int{}
		arr2 = append(arr2, arr...)

		if len(arr1) != len(arr2) {
			return false
		}

		for i, v := range arr1 {
			if v != arr2[i] {
				return false
			}
		}

		return true
}
// @lc code=end


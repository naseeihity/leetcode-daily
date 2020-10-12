/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */
package Golang

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{Val: 0}
	cur := dummy

	curry := 0
	a, b := 0, 0

	for l1 != nil || l2 != nil || curry != 0 {
		if l1 != nil {
			a = l1.Val
			l1 = l1.Next
		} else {
			a = 0
		}

		if l2 != nil {
			b = l2.Val
			l2 = l2.Next
		} else {
			b = 0
		}

		sum := a + b + curry
		num := sum % 10
		curry = sum / 10

		cur.Next = &ListNode{Val: num}
		cur = cur.Next
	}

	return dummy.Next
}

// @lc code=end

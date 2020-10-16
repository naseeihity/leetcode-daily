/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
import "strconv"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	if x < 10 {
		return true
	}

	s := strconv.Itoa(x)
	l := len(s)

	for i := 0; i <= l/2; i++ {
		if s[i] != s[l-i-1] {
			return false
		}
	}

	return true

}

// @lc code=end


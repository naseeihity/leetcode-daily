/*
 * @lc app=leetcode id=5 lang=golang
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
func longestPalindrome(s string) string {
	ans := ""
	if s == "" {
		return ans
	}

	l, r := 0, 0
	size := len(s)

	for i := 0; i <= size; i++ {
		length := max(getLen(s, i, i), getLen(s, i, i+1))
		if length > r-l {
			l = i - (length-1)/2
			r = l + length
		}
	}
	ans = string([]byte(s)[l:r])
	return ans
}

func getLen(s string, l int, r int) int {
	for l >= 0 && r < len(s) && s[l] == s[r] {
		l -= 1
		r += 1
	}
	return r - l - 1
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

// @lc code=end


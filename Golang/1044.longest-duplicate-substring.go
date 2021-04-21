/*
 * @lc app=leetcode id=1044 lang=golang
 *
 * [1044] Longest Duplicate Substring
 */

// @lc code=start
func longestDupSubstring(s string) string {
    ans := ""
		l,r := 0, len(s)

		for l < r {
			m := l + (r - l) / 2
			if m == l || m == r {
					break
			}
			dupStr := findDup(s, m)

			if dupStr == "" {
				r = m
			} else {
				l = m
				ans = dupStr
			}
		}

		return ans
}

func findDup(s string, length int) string {
	windowSize := len(s) - length
	dic := make(map[string]bool, windowSize)

	for i := 0; i <= windowSize; i++ {
		str := s[i:i+length]
		if dic[str] {
			return str
		}
		dic[str] = true
	}

	return ""
}
// @lc code=end


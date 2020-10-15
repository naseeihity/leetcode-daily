/*
 * @lc app=leetcode id=6 lang=golang
 *
 * [6] ZigZag Conversion
 */

// @lc code=start
func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	ans := make([]string, numRows)

	col, direction := 0, 1
	for i := 0; i < len(s); i++ {
		ans[col] += string(s[i])
		col += direction
		if col == 0 || col == numRows-1 {
			direction *= -1
		}
	}

	res := ""
	for i := 0; i < numRows; i++ {
		res += ans[i]
	}

	return res
}

// @lc code=end


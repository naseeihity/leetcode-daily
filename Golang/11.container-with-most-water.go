/*
 * @lc app=leetcode id=11 lang=golang
 *
 * [11] Container With Most Water
 */

// @lc code=start
func maxArea(height []int) int {
	ans := 0
	l, r := 0, len(height)-1

	for l < r {
		ans = max(ans, min(height[r], height[l])*(r-l))
		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
		}
	}

	return ans
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func min(a int, b int) int {
	if a >= b {
		return b
	}
	return a
}

// @lc code=end


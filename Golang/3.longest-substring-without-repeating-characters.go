/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	window := make(map[byte]int)
	left, right, maxLen := 0, 0, 0
	size := len(s)

	for right < size {
		cur := s[right]
		right += 1
		if _, ok := window[cur]; ok {
			window[cur] += 1
		} else {
			window[cur] = 1
		}

		for window[cur] > 1 {
			out := s[left]
			left += 1
			window[out] -= 1
		}

		maxLen = max(maxLen, right-left)
	}
	return maxLen
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
} // @lc code=end


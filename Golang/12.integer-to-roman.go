import "strings"

/*
 * @lc app=leetcode id=12 lang=golang
 *
 * [12] Integer to Roman
 */

// @lc code=start
func intToRoman(num int) string {
	s := ""
	dict := map[int]string{
		1:    "I",
		5:    "V",
		10:   "X",
		50:   "L",
		100:  "C",
		500:  "D",
		1000: "M",
	}

	a, b := 1, 5

	for num != 0 {
		k := num % 10
		num = num / 10

		if k > 0 && k < 4 {
			s = strings.Repeat(dict[a], k) + s
		} else if k == 4 {
			s = dict[a] + dict[b] + s
		} else if k == 5 {
			s = dict[b] + s
		} else if k > 5 && k < 9 {
			s = dict[b] + strings.Repeat(dict[a], k-5) + s
		} else if k == 9 {
			s = dict[a] + dict[a*10] + s
		}

		a, b = a*10, b*10
	}

	return s
}

// @lc code=end


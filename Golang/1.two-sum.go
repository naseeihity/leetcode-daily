/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)

	for idx, val := range nums {
		k := target - val
		if _, ok := dict[k]; !ok {
			dict[val] = idx
		} else {
			return []int{dict[k], idx}
		}
	}

	return nil
}

// @lc code=end


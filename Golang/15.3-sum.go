/*
 * @lc app=leetcode id=15 lang=golang
 *
 * [15] 3Sum
 */

import (
	"sort"
)

// @lc code=start
func threeSum(nums []int) [][]int {
	ans := [][]int{}
	sort.Ints(nums)

	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left, right := i+1, len(nums)-1

		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum < 0 {
				left += 1
			} else if sum > 0 {
				right -= 1
			} else {
				ans = append(ans, []int{nums[i], nums[left], nums[right]})

				for left < right && nums[left] == nums[left+1] {
					left += 1
				}

				for left < right && nums[right] == nums[right-1] {
					right -= 1
				}

				left += 1
				right -= 1
			}
		}
	}

	return ans
}

// @lc code=end


import "math"

/*
 * @lc app=leetcode id=4 lang=golang
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	n1, n2 := len(nums1), len(nums2)

	if n1 > n2 {
		return findMedianSortedArrays(nums2, nums1)
	}

	k := (n1 + n2 + 1) / 2
	l, r := 0, n1-1

	for l <= r {
		mid := l + (r-l)/2
		mid2 := k - mid - 1
		if nums1[mid] < nums2[mid2] {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}

	m1 := l
	m2 := k - l
	smallest := math.Inf(-1)
	num1, num2 := smallest, smallest
	if m1 > 0 {
		num1 = float64(nums1[m1-1])
	}
	if m2 > 0 {
		num2 = float64(nums2[m2-1])
	}
	median1 := math.Max(num1, num2)
	if (n1+n2)%2 == 1 {
		return median1
	}

	biggest := math.Inf(1)
	num3, num4 := biggest, biggest

	if m1 < n1 {
		num3 = float64(nums1[m1])
	}
	if m2 < n2 {
		num4 = float64(nums2[m2])
	}
	median2 := math.Min(float64(num3), float64(num4))

	return (median1 + median2) / 2
}

// @lc code=end


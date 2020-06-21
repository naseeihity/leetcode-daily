#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


class Solution:
    def findRow(self, matrix, target):
        top, bottom = 0, len(matrix) - 1
        col = len(matrix[0]) - 1

        while top <= bottom:
            mid = top + (bottom-top) // 2
            if matrix[mid][0] <= target <= matrix[mid][col]:
                return mid
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][col]:
                top = mid + 1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row = self.findRow(matrix, target)

        if row == -1:
            return False

        array = matrix[row]

        l, r = 0, len(array) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if array[mid] == target:
                return True
            if array[mid] < target:
                l = mid + 1
            elif array[mid] > target:
                r = mid - 1

        return False
# @lc code=end

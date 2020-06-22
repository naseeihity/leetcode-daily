#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            _target = target - numbers[i]
            l, r = i+1, len(numbers) - 1

            while l <= r:
                mid = l + (r-l) // 2
                if _target == numbers[mid]:
                    return [i+1, mid+1]
                elif _target < numbers[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return [-1, -1]
    # two pointers
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     l, r = 0, len(numbers) - 1

    #     while l <= r:
    #         total = numbers[l] + numbers[r]
    #         if total > target:
    #             r = r - 1
    #         elif total < target:
    #             l = l + 1
    #         else:
    #             return [l+1, r+1]

    #     return [-1, -1]
    # @lc code=end

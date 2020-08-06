#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False

        bucket = collections.OrderedDict()
        bucket_size = t + 1

        for i in range(len(nums)):
            key = nums[i] // bucket_size
            if key in bucket:
                return True

            bucket[key] = nums[i]

            if key - 1 in bucket and abs(nums[i] - bucket[key-1]) <= t:
                return True
            if key + 1 in bucket and abs(nums[i] - bucket[key+1]) <= t:
                return True

            if i >= k:
                bucket.popitem(last=False)

        return False
# @lc code=end

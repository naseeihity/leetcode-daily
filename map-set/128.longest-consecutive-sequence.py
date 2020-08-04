#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        h = {}
        ans = 0
        for num in nums:
            if num in h:
                continue

            l = h.get(num-1, 0)
            r = h.get(num+1, 0)

            if l > 0 and r > 0:
                # 完整的串只关心边界上值，中间的值是错误的没有关系
                # 这里给h[num]赋值只是为了让他有值
                h[num] = h[num-l] = h[num+r] = l + r + 1
            elif l > 0:
                h[num] = h[num-l] = l + 1
            elif r > 0:
                h[num] = h[num+r] = r + 1
            else:
                h[num] = 1

            # 简化写法
            # h[num] = h[num-l] = h[num+r] = l + r + 1
            ans = max(h[num], ans)

        return ans

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     h = collections.Counter(nums)
    #     ans = 0

    #     for num in nums:
    #         if num-1 not in h:
    #             l = 1
    #             while num+1 in h:
    #                 num += 1
    #                 l += 1
    #             ans = max(ans, l)

    #     return ans
# @lc code=end

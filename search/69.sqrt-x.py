#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
# 二分查找

# @lc code=start


class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        l = 1
        r = x
        res = 1

        while (l <= r):
            mid = int((l + r) / 2)
            if mid == int((x / mid)):
                return int(mid)
            elif mid > int((x / mid)):
                r = mid - 1
            else:
                l = mid + 1
                res = mid
        return int(res)
        # @lc code=end

        # 牛顿法
        # epsilon = 1e-2
        # a = x
        # while a * a - x > epsilon:
        #     a = (a + x / a) // 2

        # return int(a)

#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x * x, (n - 1) / 2)
        return self.myPow(x*x, n / 2)

    # def myPow(self, x, n):
    #     if n < 0:
    #         x = 1 / x
    #         n = -n

    #     pow = 1
    #     while n:
    #         if n & 1:
    #             pow *= x
    #         x *= x
    #         n >>= 1
    #     return pow
        # @lc code=end

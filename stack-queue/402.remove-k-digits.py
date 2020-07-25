#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        l = len(num)
        if l == k:
            return "0"
        ans = ""

        t = 0
        for i in range(l):
            while stack and num[stack[-1]] > num[i] and t < k:
                t += 1
                stack.pop()

            stack.append(i)

        for i in range(l-k):
            ans += num[stack[i]]

        return str(int(ans))
# @lc code=end

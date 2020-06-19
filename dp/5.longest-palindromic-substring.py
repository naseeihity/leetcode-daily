#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:

    def getLen(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        l = r = 0
        for i in range(len(s)):
            length = max(self.getLen(s, i, i), self.getLen(s, i, i+1))
            if length > r - l:
                l = i - (length - 1) // 2
                r = l + length

        return s[l:r]

    # Original DP
    # n = len(s)
    #  # Form a bottom-up dp 2d array
    #   # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
    # dp = [[False] * n for _ in range(n)]

    # ans = ''
    #    # every string with one character is a palindrome
    # for i in range(n):
    #     dp[i][i] = True
    #     ans = s[i]

    # maxLen = 1
    # for start in range(n-1, -1, -1):
    #     for end in range(start+1, n):
    #         # palindrome condition
    #         if s[start] == s[end]:
    #             # if it's a two char. string or if the remaining string is a palindrome too
    #             if end - start == 1 or dp[start+1][end-1]:
    #                 dp[start][end] = True
    #                 if maxLen < end - start + 1:
    #                     maxLen = end - start + 1
    #                     ans = s[start: end + 1]

    # return ans

    # 暴力解：O(n^3)
    # def isPalindrome(self, s, l, r):
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ""

    #     ans = []
    #     size = len(s)
    #     for i in range(size):
    #         for j in range(i, size):
    #             if j - i + 1 > len(ans) and self.isPalindrome(s, i, j):
    #                 ans = s[i:j+1]

    #     return ans
# @lc code=end

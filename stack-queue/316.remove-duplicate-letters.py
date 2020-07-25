#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {}
        for k, v in enumerate(s):
            last_idx[v] = k

        stack = []
        for k, v in enumerate(s):
            if v not in stack:
                # 栈顶元素比当前元素大且在后面还会出现则出栈
                while stack and stack[-1] > v and last_idx[stack[-1]] > k:
                    stack.pop()
                stack.append(v)

        return ''.join(stack)
# @lc code=end

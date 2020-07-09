#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        word_len, word_num, s_len = len(words[0]), len(words), len(s)
        word_count = collections.Counter(words)
        ans = []

        for i in range(word_len):
            left = i
            right = i
            _counter = collections.Counter()
            count = 0

            while right + word_len <= s_len:
                cur = s[right:right+word_len]
                right = right + word_len

                if cur not in words:
                    left = right
                    count = 0
                    _counter.clear()
                else:
                    count += 1
                    _counter[cur] += 1

                    while _counter[cur] > word_count[cur]:
                        out_word = s[left:left+word_len]
                        left = left+word_len
                        _counter[out_word] -= 1
                        count -= 1

                    if count == word_num:
                        ans.append(left)

        return ans
# @lc code=end

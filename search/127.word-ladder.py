from collections import defaultdict
#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not endWord in wordList:
            return 0

        wordDict = defaultdict(list)
        queue = []
        visited = set()
        visited.add(beginWord)
        size = len(beginWord)

        for word in wordList:
            for i in range(size):
                wordDict[word[:i] + "*" + word[i+1:]].append(word)

        queue.append((beginWord, 1))

        while queue:
            cur, level = queue.pop(0)

            for i in range(size):
                _word = cur[:i] + "*" + cur[i+1:]
                for word in wordDict[_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))

                wordDict[_word] = []

        return 0
# @lc code=end

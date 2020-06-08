from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if not beginWord or not endWord or not endWord in wordList:
            return []

        wordSet = set(wordList)
        size = len(beginWord)

        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = defaultdict(list)
            for cur in layer:
                if cur == endWord:
                    return layer[cur]
                for i in range(size):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word = cur[:i] + c + cur[i+1:]
                        if word in wordSet:
                            newLayer[word] += [j + [word]
                                               for j in layer[cur]]

            wordSet -= set(newLayer.keys())

            layer = newLayer

        return []

from collections import defaultdict, deque


class Solution:

    #     # BFS(build path tree) + DFS(track back)
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if not endWord in wordList:
            return []
        wordDict = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                wordDict[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque()
        visited = set()
        # curWord, depth
        depth = 1
        queue.append((beginWord, depth))
        visited.add(beginWord)
        found = False
        ans = []

        # use BFS to build the relation of nodes, parents[dog] = [log, cog]
        parents = defaultdict(set)

        while queue and not found:
            newVisted = set()
            for _ in range(len(queue)):
                cur, depth = queue.popleft()

                for i in range(L):
                    key = cur[:i] + "*" + cur[i+1:]
                    for _word in wordDict[key]:
                        if _word not in visited:
                            newVisted.add(_word)
                            parents[_word].add(cur)
                            if _word == endWord:
                                found = True
                            queue.append((_word, depth+1))

            visited = visited.union(newVisted)

        def dfs(node, path, depth):
            if depth == 0:
                if path[-1] == beginWord:
                    # 逆序后添加到ans
                    ans.append(path[::-1])
                return
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, depth-1)
                # 还原现场
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans


# class Solution:

#     # Only BFS
#     def findLadders(self, beginWord: str, endWord: str, wordList):
#         if not endWord in wordList:
#             return []

#         # {*og: [dog, log]}
#         wordDict = defaultdict(list)
#         L = len(beginWord)
#         for word in wordList:
#             for i in range(L):
#                 wordDict[word[:i] + "*" + word[i+1:]].append(word)

#         queue = deque()
#         visited = set()
#         # curWord, path
#         queue.append((beginWord, [beginWord]))
#         visited.add(beginWord)

#         found = False
#         ans = []

#         while queue and not found:
#             # only marked as visited when finish scan a layer
#             newVisted = set()
#             for _ in range(len(queue)):
#                 cur, path = queue.popleft()
#                 # when find endword, then jumpout while loop after record all ans
#                 if cur == endWord:
#                     found = True
#                     ans.append(path)
#                 else:
#                     for i in range(L):
#                         key = cur[:i] + "*" + cur[i+1:]
#                         for _word in wordDict[key]:
#                             if _word not in visited:
#                                 newVisted.add(_word)
#                                 # record path
#                                 queue.append((_word, path + [_word]))
#             visited = visited.union(newVisted)

#         return ans

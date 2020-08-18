#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start


class Solution:
    def swap(self, string, index1, index2):
        arr = list(string)
        arr[index1], arr[index2] = arr[index2], arr[index1]
        return ''.join(arr)

    def slidingPuzzle(self, board):
        goal = "123450"
        cur = ""
        for i in range(2):
            for j in range(3):
                cur += str(board[i][j])
        if cur == goal:
            return 0
        neigbours = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        steps = 0
        visited = set()
        visited.add(cur)
        queue = []
        queue.append((cur, cur.index('0')))

        while queue:
            steps += 1
            size = len(queue)
            for _ in range(size):
                curstr, zeropos = queue.pop(0)
                for pos in neigbours[zeropos]:
                    newstr = self.swap(curstr, zeropos, pos)
                    if newstr in visited:
                        continue
                    if newstr == goal:
                        return steps

                    visited.add(newstr)
                    queue.append((newstr, pos))

        return -1


test = Solution()
print(test.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
# @lc code=end

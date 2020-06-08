#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start


class Solution:

    def changeOne(self, cur, pos):
        adjacent = []
        if cur[pos] == '0':
            adjacent.append(cur[0:pos] + '9' + cur[pos+1:])
            adjacent.append(cur[0:pos] + '1' + cur[pos+1:])
        elif cur[pos] == '9':
            adjacent.append(cur[0:pos] + '0' + cur[pos+1:])
            adjacent.append(cur[0:pos] + '8' + cur[pos+1:])
        else:
            adjacent.append(cur[0:pos] + str(int(cur[pos])+1) + cur[pos+1:])
            adjacent.append(cur[0:pos] + str(int(cur[pos])-1) + cur[pos+1:])

        return adjacent[0], adjacent[1]

    def openLock(self, deadends, target: str) -> int:
        if target in deadends or not target:
            return -1

        queue = []
        visited = set()
        head = "0000"

        queue.append(head)
        visited.add(head)

        for deadend in deadends:
            visited.add(deadend)

        step = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                cur = queue.pop(0)

                if cur == target:
                    return step
                if cur in deadends:
                    continue

                for j in range(4):
                    next1, next2 = self.changeOne(cur, j)
                    if not next1 in visited:
                        visited.add(next1)
                        queue.append(next1)
                    if not next2 in visited:
                        visited.add(next2)
                        queue.append(next2)

            step += 1

        return -1

# @lc code=end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

# DFS:
# def dfs(self, grid, i, j):
#         grid[i][j] = "0"
#         for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
#             if 0 <= x < self.h and 0 <= y < self.w and grid[x][y] == "1":
#                 self.dfs(grid, x, y)

#     def numIslands(self, grid: List[List[str]]) -> int:
#         h = len(grid)
#         if h == 0:
#             return 0
#         w = len(grid[0])
#         self.h = h
#         self.w = w
#         sum = 0

#         for i in range(h):
#             for j in range(w):
#                 if grid[i][j] == "1":
#                     sum+=1
#                     self.dfs(grid, i, j)

#         return sum


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        queue = []
        sum = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    sum += 1
                    queue.append((i, j))
                    grid[i][j] = "0"
                    while queue:
                        cur_i, cur_j = queue.pop(0)
                        if cur_i-1 >= 0 and grid[cur_i-1][cur_j] == "1":
                            queue.append((cur_i-1, cur_j))
                            grid[cur_i-1][cur_j] = "0"
                        if cur_i+1 < h and grid[cur_i+1][cur_j] == "1":
                            queue.append((cur_i+1, cur_j))
                            grid[cur_i+1][cur_j] = "0"
                        if cur_j-1 >= 0 and grid[cur_i][cur_j-1] == "1":
                            queue.append((cur_i, cur_j-1))
                            grid[cur_i][cur_j-1] = "0"
                        if cur_j+1 < w and grid[cur_i][cur_j+1] == "1":
                            queue.append((cur_i, cur_j+1))
                            grid[cur_i][cur_j+1] = "0"

        return sum
# @lc code=end

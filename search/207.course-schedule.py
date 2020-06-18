#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = [0 for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            course[prerequisites[i][0]] += 1

        visited = []
        for i in range(len(course)):
            if course[i] == 0:
                visited.append(i)

        count = 0
        while visited:
            count += 1
            cur = visited.pop()

            for i in range(len(prerequisites)):
                if cur == prerequisites[i][1]:
                    course[prerequisites[i][0]] -= 1
                    if course[prerequisites[i][0]] == 0:
                        visited.append(prerequisites[i][0])

        return count == numCourses
# @lc code=end

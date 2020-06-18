#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = [0 for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            course[prerequisites[i][0]] += 1

        visited = []
        for i in range(len(course)):
            if course[i] == 0:
                visited.append(i)

        count = 0
        ans = []
        while visited:
            count += 1
            cur = visited.pop()
            ans.append(cur)

            for i in range(len(prerequisites)):
                if cur == prerequisites[i][1]:
                    course[prerequisites[i][0]] -= 1
                    if course[prerequisites[i][0]] == 0:
                        visited.append(prerequisites[i][0])

        return ans if count == numCourses else []
# @lc code=end

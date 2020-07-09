#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        start = 0
        candidates.sort()

        def dfs(candidates, target, cur, ans, start):
            if target == 0:
                ans.append(cur)
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(candidates, target -
                    candidates[i], cur+[candidates[i]], ans, i)

        dfs(candidates, target, [], ans, start)
        return ans
# @lc code=end

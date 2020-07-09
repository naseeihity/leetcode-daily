#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        start = 0
        candidates.sort()

        def dfs(candidates, target, cur, ans, start):
            if target == 0:
                ans.add(tuple(cur))
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(candidates, target -
                    candidates[i], cur+[candidates[i]], ans, i+1)

        dfs(candidates, target, [], ans, start)
        return list(ans)

        # ans = []
        # start = 0
        # candidates.sort()

        # def dfs(candidates, target, cur, ans, start):
        #     if target == 0:
        #         ans.append(cur)
        #         return

        #     for i in range(start, len(candidates)):
        #         if candidates[i] > target:
        #             break
        #         if i > start and candidates[i] == candidates[i-1]:
        #             continue
        #         dfs(candidates, target -
        #             candidates[i], cur+[candidates[i]], ans, i+1)

        # dfs(candidates, target, [], ans, start)
        # return ans
# @lc code=end

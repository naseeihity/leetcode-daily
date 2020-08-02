class Solution:

    def dfs(self, nums, used, idx, target):
        if target == 0:
            return True

        for i in range(idx, -1, -1):
            if not used[i] and nums[i] <= target:
                used[i] = True
                find = self.dfs(nums, used, i-1, target-nums[i])
                if find:
                    return True
                used[i] = False

        return False

    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        slide, temp = divmod(sum(nums), 4)
        if temp != 0:
            return False

        for num in nums:
            if num > slide:
                return False

        nums.sort()

        used = [False]*len(nums)

        for k in range(3):
            for i in range(len(nums)-1, -1, -1):
                if not used[i]:
                    used[i] = True
                    find = self.dfs(nums, used, i-1, slide-nums[i])
                    if not find:
                        return False
                    else:
                        break
        return True

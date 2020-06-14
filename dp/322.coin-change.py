#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    # BFS
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        queue = []
        ans = 0
        visited = set()
        queue.append(0)
        visited.add(0)

        while queue:
            sub_queue = []
            ans += 1
            for i in queue:
                for coin in coins:
                    val = i + coin
                    if val == amount:
                        return ans
                    if val > amount:
                        continue
                    elif val not in visited:
                        visited.add(val)
                        sub_queue.append(val)
            queue = sub_queue

        return -1

    # DP
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if not amount:
    #         return 0
    #     if not coins:
    #         return -1

    #     dp = [amount+1 for _ in range(amount+1)]
    #     dp[0] = 0
    #     for i in range(1, amount+1):
    #         for j in range(len(coins)):
    #             if i - coins[j] >= 0:
    #                 dp[i] = min(dp[i], dp[i - coins[j]]+1)

    #     return dp[amount] if dp[amount] <= amount else -1
# @lc code=end

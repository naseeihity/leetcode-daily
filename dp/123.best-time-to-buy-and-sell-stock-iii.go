package dp

func maxProfit1(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}

	k := 2
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, k+1)
		for j := 0; j < k+1; j++ {
			dp[i][j] = make([]int, 2)
		}
	}

	for i := 0; i < n; i++ {
		for kk := 1; kk < k+1; kk++ {
			if i == 0 {
				dp[i][kk][0] = 0
				dp[i][kk][1] = -prices[i]
			} else {
				dp[i][kk][0] = max(dp[i-1][kk][0], dp[i-1][kk][1]+prices[i])
				dp[i][kk][1] = max(dp[i-1][kk][1], dp[i-1][kk-1][0]-prices[i])
			}
		}
	}

	return dp[n-1][k][0]
}

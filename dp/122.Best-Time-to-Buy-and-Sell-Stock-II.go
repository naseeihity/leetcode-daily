package dp

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}

	sell, hold := 0, -prices[0]

	for i := 1; i < n; i++ {
		sell = max(sell, hold+prices[i])
		hold = max(hold, sell-prices[i])
	}

	return sell
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

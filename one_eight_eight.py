class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if k >= N/2:
            return self.greedy(N, prices)
        dp = [[0] * N for _ in range(k + 1)]
        for i in range(1, k + 1):
            curMax = dp[i][0] - prices[0]
            for j in range(1, N):
                dp[i][j] = max(dp[i][j-1], prices[j] + curMax)
                curMax = max(curMax, dp[i-1][j] - prices[j])
        return dp[k][N-1]

    def greedy(self, N, prices):
        profit = 0
        for i in range(1, N):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

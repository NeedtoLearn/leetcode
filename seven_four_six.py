class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0, 0]
        for i in range(2, n + 1):
            dp.append(min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2]))
        return dp[n]


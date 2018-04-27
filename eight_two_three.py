class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp[v] is num of btrees with root is v
        dp = {}
        A.sort()
        setA = set(A)
        for idx, v in enumerate(A):
            # Tree with node itself
            dp[v] = 1
            # Check for smaller numbers
            for u in A[:idx]:
                # Found two numbers in A whose product equal to v
                if v % u == 0 and v/u in setA:
                    dp[v] += dp[u] * dp[v/u]
        return sum(dp.values()) % (10 ** 9 + 7)
        
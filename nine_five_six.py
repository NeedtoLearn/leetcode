class Solution(object):
    def tallestBillboard(self, rods):
        """ Always maintain 2 set of rods (S1 & S2), and keep tracks of
        dp[d] = a where d = sum(S2) - sum(S1), and sum(S1) = a with assumption
        that sum(S1) <= sum(S2). So, for every rod we either add it to S1 or S2 or
        don't use it. We only care first 2 cases:
            * If rod is added to S2, the difference d will be increase by rod length
            and sum(S1) will remain the same a. But need to consider existing result to
            choose the maximum result.
            * If the rod is added to S1, the diffrence now will be abs(d - rod), and
            the new sum(S1) will be (a + rod) and sum(S2) still (a + d), so new value
            will be either min(a + rod, a + d), and we should choose the minimum.
            We still need to consider existing values as well.
        """
        dp = {0: 0}
        for rod in rods:
            for d, a in dp.items():
                dp[d + rod] = max(a, dp.get(d + rod, 0))
                dp[abs(d - rod)] = max(a + min(rod, d), dp.get(abs(d - rod), 0))
        return dp[0]


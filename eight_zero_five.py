class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return self.meetInMiddle(A)

    def meetInMiddle(self, A):
        from fractions import Fraction
        # Deduct each elem in A by its average
        N = len(A)
        S = sum(A)
        A = [a - Fraction(S, N) for a in A]
        if N == 1: return False
        # Divide A into two halves [0...N/2 -1] and [N/2...N-1]
        # Compute sum of each powerset for left half
        left = {A[0]}
        for i in xrange(1, N/2):
        	left = left | {A[i]} | {x + A[i] for x in left}
        # If there is subset sum to 0 in left, return True
        if 0 in left: return True
        # Compute sum of each powerset for right half
        right = {A[-1]}
        for i in xrange(N/2, N-1):
        	right = right | {A[i]} | {x + A[i] for x in right}
        # If there is subset sum to 0 in right, return True
        if 0 in right: return True
        # Check if there is a subset in left which combine with
        # subset in right and give sum to zero, but it cannot contain
        # all elements in left and right half.
        sleft = sum(A[:N/2])
        sright = sum(A[N/2:])
        return any(-l in right and (l, -l) != (sleft, sright) for l in left)

    def hasSubsetSum(self, A, S):
        return self.hasSubsetSumDP(A, S)

    def hasSubsetSumRecursive(self, A, S):
        if S == 0:
            return True
        if not A:
            return False
        # If first element > S, ignore it
        if A[0] > S:
            return self.hasSubsetSumRecursive(A[1:], S)
        # Consider two case whether first elem is chosen
        return self.hasSubsetSumRecursive(A[1:], S-A[0]) or \
                    self.hasSubsetSumRecursive(A[1:], S)

    def hasSubsetSumDP(self, A, S):
        N = len(A)
        # Create dp array store dp[i][s] - boolean,
        # if A[0:i] elements has subset sum to s
        dp = [[False] * (S+1) for i in range(N+1)]
        # Empty set only match with zero sum
        dp[0][0] = True
        for i in range(1, N+1):
            for s in range(1, S+1):
                dp[i][s] = dp[i-1][s] or (A[i-1] == s) or (A[i-1] < S and dp[i-1][s-A[i-1]])
        return dp[N][S]


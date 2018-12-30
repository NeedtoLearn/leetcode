class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        A.sort()
        curMin = A[-1] - A[0]
        for i in range(N-1):
            curMin = min(curMin, max(A[-1]-K, A[i]+K) - min(A[0]+K, A[i+1]-K))
        return curMin

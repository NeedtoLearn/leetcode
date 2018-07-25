class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp(n)
    
    def recur(self, n):
        if n <= 1:
            return 1
        count = 0
        for i in range(1, n+1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        return count

    def dp(self, n):
        m = [0] * (n + 1)
        m[0] = m[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                m[i] += m[j-1] * m[i-j]
        return m[n]
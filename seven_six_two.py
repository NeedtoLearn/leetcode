class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        for i in range(L, R+1):
            if self.isPrime(bin(i).count('1')):
                ans += 1
        return ans

    def isPrime(self, n):
        if n == 1:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True


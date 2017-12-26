class Solution(object):
    def crackSafe(self, n, k):
        """
        Combinations of lock satisfy De Bruijn sequence, so
        next lock can share n-1 digits with previous lock.
        :type n: int
        :type k: int
        :rtype: str
        """
        password = start = '0' * n
        pwd_length = k**n + n - 1
        return self.dfs(password, pwd_length, start, n, k)

    def dfs(self, password, pwd_length, start, n , k):
        if len(password) == pwd_length:
            return password
        for i in range(k):
            new_num = start[1:] + str(i)
            if new_num not in password:
                result = self.dfs(password + str(i), new_num, n, k)
                if result:
                    return result

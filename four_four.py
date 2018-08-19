class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.dpSol(s, p)
 
    def recurSol(self, s, p):
        if not s:
            return all(c == '*' for c in p)
        if not p:
            return not s
        if p[0] == '?' or p[0] == s[0]:
            return self.recurSol(s[1:], p[1:])
        if p[0] == '*':
            return self.recurSol(s, p[1:]) or self.recurSol(s[1:], p)
        return False

    def dpSol(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*':
                dp[0][i+1] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[m][n]

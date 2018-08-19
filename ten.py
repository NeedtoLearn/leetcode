class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.dpSol(s, p)

    def recurSol(self, s, p):
        if not p:
            return not s
        first_match = bool(s) and p[0] in ('.', s[0])
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        if first_match:
            return self.isMatch(s[1:], p[1:])
        return False

    def dpSol(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    prev_match = (i > 0) and p[j-2] in ('.', s[i-1])
                    dp[i][j] = dp[i][j-2] or (prev_match and dp[i-1][j])
                else:
                    next_match = (i > 0) and p[j-1] in ('.', s[i-1])
                    dp[i][j] = next_match and dp[i-1][j-1]
        return dp[m][n]

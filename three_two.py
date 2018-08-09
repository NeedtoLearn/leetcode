class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        N = len(s)
        dp = [0] * N
        for i in range(1, N):
            j = i - dp[i-1] - 1
            if j >= 0 and s[i] == ')' and s[j] == '(':
                dp[i] = dp[i-1] + 2
                if j > 0:
                    dp[i] += dp[j-1]
            else:
                dp[i] = 0
        return max(dp)

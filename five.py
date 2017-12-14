class Solution(object):

    def longestPalindrome(self, s):
        n = len(s)
        cur_pal = s[0] if s else ''
        for i in range(len(s)):
            if i < n - 1:
                new_pal = self.helper(s, i, i + 1, '')
                if len(new_pal) > len(cur_pal):
                    cur_pal = new_pal
            if i < n - 2:
                new_pal = self.helper(s, i, i + 2, s[i+1])
                if len(new_pal) > len(cur_pal):
                    cur_pal = new_pal
        return cur_pal

    def helper(self, s, start, end, pal):
        if start < 0 or end >= len(s) or s[start] != s[end]:
            return pal
        return self.helper(s, start - 1, end + 1, s[start:end+1])

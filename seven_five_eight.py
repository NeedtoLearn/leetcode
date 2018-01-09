class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        n = len(S)
        # Construct mask for bold characters
        mask = [False] * n
        for word in words:
            idx = S.find(word, 0)
            while idx >= 0:
                for i in range(idx, idx + len(word)):
                    mask[i] = True
                idx = S.find(word, idx + 1)
        # Construct new string with <b> tags
        newS = ''
        for i in range(n):
            if mask[i] and (i == 0 or not mask[i-1]):
                newS += '<b>'
            newS += S[i]
            if mask[i] and (i == n-1 or not mask[i+1]):
                newS += '</b>'
        return newS



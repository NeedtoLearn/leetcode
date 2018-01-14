class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        acc = start = 0
        # Split S into special substrings
        for i, v in enumerate(S):
            acc = acc + 1 if v == '1' else acc - 1
            # Found a special substring
            if acc == 0:
                res.append('1' + self.makeLargestSpecial(S[start+1:i]) + '0')
                start = i + 1
        return ''.join(sorted(res, reverse=True))


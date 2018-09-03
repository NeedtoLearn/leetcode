class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        groups = set()
        for s in A:
            # Split to two substrings with odd and even indexes
            even, odd = ''.join(sorted(s[::2])), ''.join(sorted(s[1::2]))
            groups.add((even, odd))
        return len(groups)

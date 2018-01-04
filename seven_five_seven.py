class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans = 0
        acc = [2] * len(intervals)
        intervals.sort(key= lambda (s, e): (s, -e))
        while intervals:
            (s, e), t = intervals.pop(), acc.pop()
            for i in xrange(s, s + t):
                for j, (s0, e0) in enumerate(intervals):
                    if i <= e0:
                        acc[j] -= 1
                ans += 1
        return ans


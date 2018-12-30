class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.N = len(persons)
        self.persons = persons
        self.times = times
        self.dp = self.cal_dp()

    def cal_dp(self):
        dp = []
        count = [0] * (self.N + 2)
        for person in self.persons:
            count[person] += 1
            if dp and count[dp[-1]] > count[person]:
                dp.append(dp[-1])
            else:
                dp.append(person)
        return dp

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.dp[bisect.bisect(self.times, t) - 1]        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

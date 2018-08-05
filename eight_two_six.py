class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # dp[i] store the largest profit for job with difficulty i
        dp = [0] * (10 ** 5 + 1)
        # Combine profit and difficulty, then sort by profit
        works = zip(profit, difficulty)
        sorted(works, reverse=True)
        # Fill dp array with greedy approach
        cur_d = 10 ** 5 + 1
        for p, d in works:
            # Make sure d is less then processed d;
            # otherwise we alr found best profit.
            if d < cur_d:
                # Fill all job with difficulty >= d
                # cause it's the best profit we can have.
                for i in range(d, cur_d):
                    dp[i] = p
                cur_d = d
        # Get best profit for each worker and sum them up
        return sum(dp[w] for w in worker)


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        friend_requests = 0
        # Sort ages in non-increasing order
        ages.sort(reverse=True)
        # For each age B find smallest age A satisfies
        # first condition using binary search
        for idxA, A in enumerate(ages):
            idxB = self.findSmallestB(ages, A, idxA, len(ages) - 1)
            friend_requests += idxB - idxA
        # Handle duplicate ages
        friend_requests += self.computeRequestForSameAge(ages)
        return friend_requests

    def findSmallestB(self, ages, A, start, end):
        if start >= end:
            return end
        mid = (start + end + 1) / 2
        # B can make friend with A if reverse first condition is true
        if ages[mid] > A * 0.5 + 7:
            return self.findSmallestB(ages, A, mid, end)
        else:
            return self.findSmallestB(ages, A, start, mid - 1)

    def computeRequestForSameAge(self, ages):
        # Calculate duplicates for each age
        dups = [0] * 121
        for age in ages:
            dups[age] += 1
        # Compute friend requests for each duplicate age
        # Note: only age above 15 can make friend with same age
        # due to first constraint. (B > 0.5*A + 7 => B > 15 cause A == B)
        friend_requests = 0
        for age in range(15, 121):
            # Number of friend requests at age N is N * (N-1) / 2 or (0 + 1 + ... + N - 1)
            # Because each guy will be friend with all guys behind it.
            friend_requests += dups[age] * (dups[age] - 1) / 2
        return friend_requests

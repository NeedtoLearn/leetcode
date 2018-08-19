class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1
        if i == j:
            boats += 1
        return boats


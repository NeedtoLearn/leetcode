from collections import deque

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Make sure negative numbers come first
        A.sort(key=lambda x: (abs(x), x))
        # Keep track of smallest numbers
        queue = deque()
        for num in A:
            if not queue or num != 2 * queue[0]:
                queue.append(num)
            else:
                queue.popleft()
        return not queue

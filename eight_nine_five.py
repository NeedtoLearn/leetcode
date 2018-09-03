import heapq


class FreqStack(object):

    def __init__(self):
        self.cur_idx = 0
        self.data = []
        self.count = {}

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.cur_idx += 1
        self.count[x] = self.count.get(x, 0) + 1
        # Negate value to create max heap
        heapq.heappush(self.data, (-self.count[x], -self.cur_idx, x))

    def pop(self):
        """
        :rtype: int
        """
        _, _, val = heapq.heappop(self.data)
        self.count[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
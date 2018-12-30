class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        # Perform BFS to find first island, and its surrounding 0s
        first_one = self.findFirstOne(A, N)
        visited = {first_one}
        surrounds = set()
        queue = [first_one]
        while queue:
            u = queue[0]
            queue = queue[1:]
            for v in self.getNeighbors(u, N):
                if v not in visited:
                    r, c = v
                    if A[r][c] == 1:
                        queue.append(v)
                        visited.add(v)
                    else:
                        surrounds.add(v)
        # Perform BFS to find shortest path to second island
        queue = [(r, c, 1) for r, c in surrounds]
        while queue:
            r, c, d = queue[0]
            queue = queue[1:]
            for v in self.getNeighbors((r, c), N):
                if v not in visited:
                    r, c = v
                    if A[r][c] == 1:
                        return d
                    queue.append((r, c, d+1))
                    visited.add((r, c))
        return -1

    def getNeighbors(self, u, N):
        neighs = set()
        r, c = u
        if r > 0:
            neighs.add((r-1, c))
        if r + 1 < N:
            neighs.add((r+1, c))
        if c > 0:
            neighs.add((r, c-1))
        if c + 1 < N:
            neighs.add((r, c + 1))
        return neighs
    
    def findFirstOne(self, A, N):
        for r in range(N):
            for c in range(N):
                if A[r][c] == 1:
                    return r, c

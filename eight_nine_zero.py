class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        return self.graphSol(N, dislikes)

    def graphSol(self, N, dislikes):
        # Construct graph from dislikes
        adjList = [set() for _ in range(N + 1)]
        for p1, p2 in dislikes:
            # Undirected graph
            adjList[p1].add(p2)
            adjList[p2].add(p1)
        # Group people base on graph
        groups = [-1] * (N + 1)
        visited = set()
        for i in range(1, N + 1):
            if i not in visited:
                # Perform BFS for each component
                if not self.bfs(adjList, i, visited, groups):
                    return False
        return True

    def bfs(self, graph, start, visited, groups):
        groups[start] = 1
        queue = [start]
        while queue:
            u = queue[0]
            queue = queue[1:]
            visited.add(u)
            for v in graph[u]:
                if groups[v] < 0:
                    queue.append(v)
                    groups[v] = 2 if groups[u] == 1 else 1
                elif groups[u] == groups[v]:
                    return False
        return True

    def recurSol(self, dislikes, G1, G2):
        if not dislikes:
            return True
        p1, p2 = dislikes[0]
        if p1 in G1:
            if p2 in G1:
                return False
            G2.add(p2)
            return self.recurSol(dislikes[1:], G1, G2)
        elif p1 in G2:
            if p2 in G2:
                return False
            G1.add(p2)
            return self.recurSol(dislikes[1:], G1, G2)
        else:
            if p2 in G1:
                G2.add(p1)
                return self.recurSol(dislikes[1:], G1, G2)
            elif p2 in G2:
                G1.add(p1)
                return self.recurSol(dislikes[1:], G1, G2)
            else:
                return self.recurSol(dislikes[1:], G1 | {p1}, G2 | {p2}) or self.recurSol(dislikes[1:], G1 | {p2}, G2 | {p1})

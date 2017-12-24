class Solution(object):

    INFINITY = 1000000

    def networkDelayTime(self, times, N, K):
        """
        This problem is a directed and weighted graph,
        and find the maximum distance from source node.
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Build graph using adjacent matrix
        graph = [[self.INFINITY for c in range(N)] for r in range(N)]
        for (u, v, w) in times:
            # Directed graph
            graph[u-1][v-1] = w
        # Use appropriate algo to find shortest path
        return self.dijkstra(graph, K- 1, N)

    def floyd_warshall(self, distance, source, N):
        # Each pair (u, v), if there is vertex w such
        # path from u to v through w is shorter than current
        # path, update it
        for w in range(N):
            for u in range(N):
                for v in range(N):
                    if distance[u][w] + distance[w][v] < distance[u][v]:
                        distance[u][v] = distance[u][w] + distance[w][v]
        # Search for node with longest distance from source
        cost = max(distance[source][:source] + distance[source][source+1:])
        return cost if cost != self.INFINITY else -1

    def dijkstra(self, graph, source, N):
        distances = [self.INFINITY for i in range(N)]
        distances[source] = 0
        visited = set()
        while len(visited) < N:
            # Find next node with min distance to source node
            next_node, next_dist = self._get_next_node(distances, visited, N)
            if next_node < 0:
                return -1
            visited.add(next_node)
            # Update distance for next node's neighbors
            for i in range(N):
                if distances[next_node] + graph[next_node][i] < distances[i]:
                    distances[i] = distances[next_node] + graph[next_node][i]
        # Return maximum travelling time
        return max(distances[:source] + distances[source+1:])

    def _get_next_node(self, distances, visited, N):
        cur_node = -1
        cur_dist = self.INFINITY
        for i in range(N):
            if i not in visited and distances[i] < cur_dist:
                cur_node = i
                cur_dist = distances[i]
        return cur_node, cur_dist


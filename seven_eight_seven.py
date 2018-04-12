from Queue import PriorityQueue

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # Using modified Dijkstra with depth param
        # Construct adjacent matrix
        adj_mat = [[-1] * n for i in range(n)]
        for u, v, price in flights:
            adj_mat[u][v] = price
        # Initialize priority queue to store
        # distances with format (price, city, stops).
        priority_queue = PriorityQueue()
        priority_queue.put((0, src, -1))
        # Create list to store price from src to each city
        prices = [-1 for i in range(n)]
        while not priority_queue.empty():
            price, city, stops = priority_queue.get()
            # Only accept the flight if stops <= K
            if stops <= K:
                # If city is destination, then we found cheapest price
                if city == dst:
                    return price
                # Update price for the city
                prices[city] = price
                # Add neighbors of city to priority queue
                for i in range(n):
                    if adj_mat[city][i] != -1:
                        priority_queue.put((price + adj_mat[city][i], i, stops + 1))
        return -1

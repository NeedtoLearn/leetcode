class Solution(object):

    MAPPER = {
        '0': ['1', '9'],
        '1': ['2', '0'],
        '2': ['3', '1'],
        '3': ['4', '2'],
        '4': ['5', '3'],
        '5': ['6', '4'],
        '6': ['7', '5'],
        '7': ['8', '6'],
        '8': ['9', '7'],
        '9': ['0', '8'],
    }

    def openLock(self, deadends, target):
        """
        Using modified BFS to find shortest path to target.
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        generated = set(deadends)
        generated.add('0000')
        queue = [('0000', 0)]
        while queue:
            u, depth = queue[0]
            queue = queue[1:]
            for v in self._get_neighbors(u):
                if v == target:
                    return depth+1
                if v not in generated:
                    generated.add(v)
                    queue.append((v, depth+1))
        return -1

    def _get_neighbors(self, wheels):
        neighbors = []
        for i in range(4):
            for num in self.MAPPER[wheels[i]]:
                neighbors.append(wheels[:i] + num + wheels[i+1:])
        return neighbors


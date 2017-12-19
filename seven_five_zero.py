class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(i+1, rows):
                # Fix two rows, then scan through each column to find pairs of 1
                pairs = 0
                for c in range(cols):
                    if grid[i][c] and grid[j][c]:
                        pairs += 1
                # Pick any 2 pairs
                count += pairs*(pairs-1)/2
        return count


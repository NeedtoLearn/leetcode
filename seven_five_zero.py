class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    for i in range(c+1, cols):
                        if grid[r][i]:
                            for j in range(r+1, rows):
                                if grid[j][c] and grid[j][i]:
                                    count += 1
        return count


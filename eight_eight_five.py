class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        coords = [[r0, c0]]
        curRadius = 0
        curR = r0
        curC = c0
        curDir = 'R'
        while curRadius < 2 * max(R, C):
            if curDir == 'R':
                curRadius += 1
                for i in range(1, curRadius + 1):
                    curC += 1
                    if 0 <= curR < R and 0 <= curC < C:
                        coords.append([curR, curC])
                curDir = 'D'
            elif curDir == 'D':
                for i in range(1, curRadius + 1):
                    curR += 1
                    if 0 <= curR < R and 0 <= curC < C:
                        coords.append([curR, curC])
                curDir = 'L'
            elif curDir == 'L':
                curRadius += 1
                for i in range(1, curRadius + 1):
                    curC -= 1
                    if 0 <= curR < R and 0 <= curC < C:
                        coords.append([curR, curC])
                curDir = 'U'
            else:
                for i in range(1, curRadius + 1):
                    curR -= 1
                    if 0 <= curR < R and 0 <= curC < C:
                        coords.append([curR, curC])
                curDir = 'R'
        return coords

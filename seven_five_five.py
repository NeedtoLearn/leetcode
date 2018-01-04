class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for i in range(V):
            idxL = self.searchMinLeft(heights, K)
            idxR = self.searchMinRight(heights, K)
            if heights[idxL] <= heights[idxR] and heights[idxL] < heights[K]:
                heights[idxL] += 1
            elif heights[idxR] < heights[idxL] and heights[idxR] < heights[K]:
                heights[idxR] += 1
            else:
                heights[K] += 1
        return heights

    def searchMinLeft(self, heights, K):
        curMin = K
        while K > 0:
            if heights[K-1] <= heights[K]:
                if heights[K-1] < heights[K]:
                    curMin = K-1
                K -= 1
            else:
                return curMin
        return curMin

    def searchMinRight(self, heights, K):
        curMin = K
        while K < len(heights) - 1:
            if heights[K+1] <= heights[K]:
                if heights[K+1] < heights[K]:
                    curMin = K + 1
                K += 1
            else:
                return curMin
        return curMin


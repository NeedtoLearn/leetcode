class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        n = len(row) / 2
        for i in range(n):
            if row[i * 2] % 2 == 0:
                partner = row[i * 2] + 1
            else:
                partner = row[i * 2] - 1
            # Check if need to swap
            if row[i * 2 + 1] != partner:
                ans += 1
                idx = row.index(partner)
                row[i * 2 + 1], row[idx] = row[idx], row[i * 2 + 1]
        return ans


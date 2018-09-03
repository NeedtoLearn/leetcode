# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        return self.recurSol(N)

    def recurSol(self, N):
        fbts = []
        if N == 1:
            return [TreeNode(0)]
        for i in range(1, N-1, 2):
            ltrees = self.allPossibleFBT(i)
            rtrees = self.allPossibleFBT(N-1-i)
            for ltree in ltrees:
                for rtree in rtrees:
                    root = TreeNode(0)
                    root.left = ltree
                    root.right = rtree
                    fbts.append(root)
        return fbts

"""
01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""


class Solution:
    def updateMatrix(self, mat):
        c = 0
        out = []
        for d1 in mat:
            o = []
            for d2 in d1:
                if d2 == 0:
                    c = 0
                else:
                    c += 1
                o.append(c)
            out.append(o)
        return out


solution = Solution()
solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])

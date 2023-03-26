"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""


class Solution:
    def rotate1(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        matrix.extend([[i[j] for i in matrix[::-1]] for j in range(len(matrix[0]))])
        for i in range(size):
            matrix.pop(0)

    def rotate(self, matrix: list) -> None:
        if any([
            matrix is None,
            len(matrix) == 0,
            len(matrix[0]) == 0
        ]):
            return
        row_number = len(matrix)
        column_number = len(matrix[0])
        first = 0
        last = row_number - 1
        while first < last:
            matrix[first], matrix[last] = matrix[last], matrix[first]
            first += 1
            last -= 1
        for i in range(0, row_number):
            for j in range(i + 1, column_number):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

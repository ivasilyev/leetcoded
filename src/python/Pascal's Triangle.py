"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

    1 <= numRows <= 30
"""


class Solution:
    def factorial(self, x: int):
        out = 1
        for i in range(1, x + 1):
            out *= i
        return out

    def _generate_number(self, row: int, column: int):
        return int(self.factorial(row) / (self.factorial(column) * self.factorial(row - column)))

    def generate(self, numRows: int) -> list:
        out = list()
        column_number = 1
        for row in range(numRows):
            tmp = list(range(column_number))
            for column in tmp:
                if column == 0 or column == column_number - 1:
                    tmp[column] = 1
                else:
                    tmp[column] = self._generate_number(row, column)
            out.append(tmp)
            column_number += 1
        return out

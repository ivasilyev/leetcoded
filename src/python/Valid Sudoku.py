"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.



Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.



Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.


"""


class Solution:
    def _get_cube_coords(self, matrix, size):
        return [(x, y) for x in range(len(matrix))[::size] for y in range(len(matrix[0]))[::size]]

    def _get_cube(self, matrix, coords: tuple, size: int):
        return [
            matrix[x][y]
            for x in range(coords[0], coords[0] + size)
            for y in range(coords[1], coords[1] + size)
        ]

    def _is_list_valid(self, x: list):
        _x = [i for i in x if str(i).isnumeric()]
        return len(_x) == len(set(_x))

    def _transpose(self, m: list):
        return [[i[j] for i in m]for j in range(len(m[0]))]

    def _are_rows_valid(self, board: list):
        return all(self._is_list_valid(row) for row in board)

    def _are_columns_valid(self, board: list):
        return all(self._is_list_valid(column) for column in self._transpose(board))

    def _are_cubes_valid(self, board: list):
        size = 3
        coords = self._get_cube_coords(board, size)
        return all(
            self._is_list_valid(self._get_cube(board, cube_anchor, size))
            for cube_anchor in coords
        )

    def isValidSudoku(self, board: list) -> bool:
        return all([
            self._are_rows_valid(board),
            self._are_columns_valid(board),
            self._are_cubes_valid(board)
        ])

"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:

Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

Example 3:

Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01

Constraints:

    1 <= n <= 30
    1 <= k <= 2n - 1
"""


class Solution:
    def kthGrammar(self, n, k):
        # Recursive
        if n == 1:
            return 0
        row = self.kthGrammar(n - 1, (k + 1) // 2)
        s = (k % 2) - 1
        if row == 0:
            if s == 0:
                return 0
            else:
                return 1
        else:
            if s == 0:
                return 1
            else:
                return 0

    def kthGrammar2(self, n: int, k: int) -> int:
        # Iterative
        symbol = 0
        number_of_elements_in_level = 1 << (n - 1)
        for _ in range(0, n - 1):
            if k > number_of_elements_in_level // 2:
                k = k - number_of_elements_in_level // 2
                symbol = 0 if symbol else 1
            number_of_elements_in_level //= 2
        return symbol

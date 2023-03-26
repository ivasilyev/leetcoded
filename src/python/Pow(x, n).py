"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

Constraints:

    -100.0 < x < 100.0
    -231 <= n <= 231-1
    n is an integer.
    -104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Recursive, Leetcode maximum recursion depth may be exceeded
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        return x * self.myPow(x, n - 1)

    def myPowDumb(self, x: float, n: int) -> float:
        return x ** n

    def myPowIter(self, x: float, n: int) -> float:
        # Iterative, Leetcode time limit may be exceeded
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = - n
        accumulator = x
        for _ in range(1, n):
            accumulator *= x
        return accumulator


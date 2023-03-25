"""
Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 3 ** 3

Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

Constraints:
    -231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""

MAX = 3 ** 19


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Recursive
        if n % 3 > 0:
            return False
        m = n / 3
        if m == 1.0:
            return True
        return self.isPowerOfThree(m)

    def isPowerOfThree3(self, n: int) -> bool:
        if n < 1:
            return False
        return MAX % n == 0

    def isPowerOfThree2(self, n: int) -> bool:
        # Iterative
        if n < 1:
            return False
        p = 0
        while True:
            if 3 ** p == n:
                return True
            if 3 ** p > n:
                return False
            p += 1

    def isPowerOfThree1(self, n: int) -> bool:
        from math import ceil, log
        try:
            g = log(n, 3)
            if 3 ** ceil(g) == n:
                return True
        except ValueError:
            return False

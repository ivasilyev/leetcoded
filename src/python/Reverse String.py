"""
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.
"""


class Solution:
    """
    Do not return anything, modify s in-place instead.
    """
    def reverseString1(self, s: list):
        s = s.reverse()

    def reverseString2(self, s: list):
        for idx, i in enumerate(s[::-1]):
            s[idx] = i

    def reverseString3(self, s: list):
        """
        Time Complexity: O(N)
        Auxiliary Space: O(1)
        """
        for idx in range(0, int(len(s) / 2)):
            tmp = s[idx]
            # Zero-based
            rev = len(s) - 1 - idx
            s[idx] = s[rev]
            s[rev] = tmp
        print(s)

    def reverseString4(self, s: list):
        """
        Time Complexity: O(N)
        Auxiliary Space: O(1)
        """
        n = len(s) - 1
        i = 0
        while i <= n:
            tmp = s[i]
            s[i] = s[n]
            s[n] = tmp
            n -= 1
            i += 1

    def recursive_body_1(self, s: list, n: int, i: int):
        if n <= i:
            return
        i_ = s[i]
        s[i] = s[n]
        s[n] = i_
        self.recursive_body_1(s, n - 1, i + 1)

    def reverseString5(self, s: list):
        """
        Time Complexity: O(N)
        Auxiliary Space: O(N)
        """
        self.recursive_body_1(s, len(s) - 1, 0)

    def recursive_body_2(self, s: list, i: int):
        n = len(s) - 1 - i
        if i > n:
            return
        i_ = s[i]
        s[i] = s[n]
        s[n] = i_
        self.recursive_body_2(s, i + 1)

    def reverseString6(self, s: list):
        """
        Time Complexity: O(N)
        Auxiliary Space: O(N)
        """
        self.recursive_body_2(s, 0)


"""
From https://linuxize.com/post/python-reverse-string/

Methods	Execution Time	Comparison Ratio Calc.
Slicing	0.23	1x
List Reverse	1.63	7x
Join & Reserved	1.73	7.5x
Recursion	19.19	83x
"""

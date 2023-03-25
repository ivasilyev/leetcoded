"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

   Hide Hint #1
Use a stack of characters.
   Hide Hint #2
When you encounter an opening bracket, push it to the top of the stack.
   Hide Hint #3
When you encounter a closing bracket, check if the top of the stack was the opening for it.
If yes, pop it from the stack. Otherwise, return false.
"""

from collections import deque


PARENTHESISES = {
    "(": ")",
    "[": "]",
    "{": "}",
}


class Solution:
    def _is_closer_valid(self, before: str, current: str):
        return current == PARENTHESISES.get(before)

    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in PARENTHESISES.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or not self._is_closer_valid(stack.pop(), char):
                    return False
        if len(stack) > 0:
            return False
        return True

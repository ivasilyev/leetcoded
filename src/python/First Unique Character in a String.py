"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        qualifier = dict()
        for char in s:
            if char in qualifier.keys():
                if not qualifier[char]:
                    continue
                qualifier[char] = False
            else:
                qualifier[char] = True
        for char in qualifier:
            if qualifier[char] is True:
                return s.index(char)
        return -1

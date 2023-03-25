"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""


class Solution:
    def _is_char_valid(self, char, idx, word):
        if idx < len(word):
            return word[idx] == char
        return False

    def longestCommonPrefix(self, strs: list) -> str:
        out = ""
        strs = sorted(strs, key=len)
        for idx, char in enumerate(strs[0]):
            if all(self._is_char_valid(char, idx, word) for word in strs[1:]):
                out += char
            else:
                break
        return out

"""
Smallest String With Swaps

You are given a string s, and an array of pairs of indices in the string pairs
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number
of times.

Return the lexicographically smallest string that s can be changed to after using
the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.

   Hide Hint #1
Think of it as a graph problem.
   Hide Hint #2
Consider the pairs as connected nodes in the graph,
what can you do with a connected component of indices ?
   Hide Hint #3
We can sort each connected component alone to get the lexicographically minimum string.
"""


from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list) -> str:
        n = len(s)
        r = list(range(n))

        def get(x):
            if r[x] != x:
                r[x] = get(r[x])
            return r[x]

        for p1, p2 in pairs:
            r[get(p1)] = get(p2)
        d = defaultdict(list)
        for idx, char in enumerate(s):
            heappush(d[get(idx)], char)
        return "".join(heappop(d[get(i)]) for i in range(n))

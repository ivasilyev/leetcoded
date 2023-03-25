"""
Number of Provinces

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities
and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

1 - 2
  3

i = 0
j = 1
c = 2

[[i, j, c], [i, j, c], [i, j, c]]

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

1 2
 3

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]

"""


class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        def dfs(x):
            for _idx in range_connection_number:
                if isConnected[x][_idx] == 1 and _idx not in visited:
                    visited.add(_idx)
                    dfs(_idx)

        visited = set()
        num = 0
        range_connection_number = range(len(isConnected[0]))
        for node in range(len(isConnected)):
            for connection in range_connection_number:
                if isConnected[node][connection] == 1 and connection not in visited:
                    visited.add(connection)
                    dfs(connection)
                    num += 1
        return num

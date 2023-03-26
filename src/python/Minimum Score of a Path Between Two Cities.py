"""
Minimum Score of a Path Between Two Cities

You are given a positive integer n representing n cities numbered from 1 to n.
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates
that there is a bidirectional road between cities ai and bi with a distance equal to distancei.
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times,
and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

Example 1:

     1
    / \
 7/    \9
4  ---  2
   5   /
      /6
     3

Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4.
The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:

   1
 4/ \2
 /   \
3     2
7\
  \
   4

Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4.
The score of this path is min(2,2,4,7) = 2.

Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.

"""


from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: list) -> int:
        # Breadth-first search
        def bfs(city):
            _min = float('inf')
            queue = deque([city, ])
            visited_cities = set()
            visited_cities.add(city)
            while queue:
                current_city = queue.popleft()

                for i, j in d[current_city]:
                    if j not in visited_cities:
                        visited_cities.add(j)
                        queue.append(j)
                    _min = min(_min, i)
            return _min

        d = defaultdict(list)
        for left, right, distance in roads:
            d[left].append([distance, right])
            d[right].append([distance, left])
        return bfs(1)

    def minScore2(self, n: int, roads: list) -> int:
        # Union-based search
        r = list(range(n + 1))

        def find(x):
            if x != r[x]:
                r[x] = find(r[x])
            return r[x]

        for i, j, _ in roads:
            if r[i] != r[j]:
                r[find(i)] = find(j)
        return min(j for i, _, j in roads if find(i) == find(1))


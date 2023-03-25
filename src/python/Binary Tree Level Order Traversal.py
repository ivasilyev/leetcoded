"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

    3
  /  \
9    20
    /  \
  15    7
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        from collections import deque
        # Queue-based
        if root is None:
            return list()
        queue = deque([root])
        out = [[root.val]]
        tmp = deque()

        while queue:
            node = queue.popleft()
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
            if not queue:
                if tmp:
                    out.append([i.val for i in tmp])
                queue = tmp
                tmp = deque()
        return out

    # Recursive
    def levelOrder1(self, root: TreeNode):
        def _helper(x: list):
            if len(x) == 0:
                return

            todo = list()
            done = list()
            for node in x:
                done.append(node.val)
                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)
            out.append(done)
            _helper(todo)
            return
        out = list()
        if root is not None:
            _helper([root])
        return out

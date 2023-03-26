"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    / \
   15  7

Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode):
        # Recursive
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left, depth_right) + 1

    def maxDepthIter(self, root: TreeNode):
        # Iterative
        if root is None:
            return 0
        accumulator = list()
        accumulator.append(root)
        out = 0
        while True:
            node_count = len(accumulator)
            if node_count == 0:
                return out
            out += 1
            while node_count > 0:
                node = accumulator[0]
                accumulator.pop(0)
                if node.left is not None:
                    accumulator.append(node.left)
                if node.right is not None:
                    accumulator.append(node.right)
                node_count -= 1

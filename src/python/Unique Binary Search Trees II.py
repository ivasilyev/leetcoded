"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]



Constraints:

    1 <= n <= 8
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _generate_trees(self, start, end):
        if start > end:
            return [None]
        trees = []
        for i in range(start, end+1):
            left_trees = self._generate_trees(start, i-1)
            right_trees = self._generate_trees(i+1, end)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    tree = TreeNode(i)
                    tree.left = left_tree
                    tree.right = right_tree
                    trees.append(tree)
        return trees

    def generateTrees(self, n: int):
        # Recursive
        if n is None:
            return list
        return self._generate_trees(1, n)

    def _clone_tree(self, root, offset):
        out = list()
        if offset < root:
            return
        if offset == root:
            out.append(TreeNode(root))
            return out
        for i in range(root, offset + 1):
            left_tree = self._clone_tree(root, i - 1)
            right_tree = self._clone_tree(i + 1, offset)
            if left_tree is not None and right_tree is not None:
                for left_sub in left_tree:
                    for right_sub in right_tree:
                        node = TreeNode(i)
                        node.left = left_sub
                        node.right = right_sub
                        out.append(node)
            elif left_tree is not None:
                for left_sub in left_tree:
                    node = TreeNode(i)
                    node.left = left_sub
                    out.append(node)
            elif right_tree is not None:
                for right_sub in right_tree:
                    node = TreeNode(i)
                    node.right = right_sub
                    out.append(node)
        return out

    def generateTrees2(self, n: int):
        # Iterative
        if n == 0:
            return list
        return self._clone_tree(1, n)

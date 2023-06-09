"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

   2
 /  \
1    3

Input: root = [2,1,3]
Output: true

Example 2:

   5
 /  \
1    4
    / \
   3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MIN = -2 ** 31 - 1
MAX = 2 ** 31


class Solution:
    def is_valid_bst(self, node: TreeNode, minimum, maximum):
        if node is None:
            return True
        if node.val <= minimum or node.val >= maximum:
            return False
        return self.is_valid_bst(node.left, minimum, node.val) and self.is_valid_bst(node.right, node.val, maximum)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, MIN, MAX)

"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

      1
    /  \
   2    2
 /  \  /  \
3   4 4    3

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

     1
   /  \
  2    2
   \    \
    3    3

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_symmetric(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val != right.val:
            return False
        else:
            return self._is_symmetric(left.left, right.right) and self._is_symmetric(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._is_symmetric(root.left, root.right)

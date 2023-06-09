"""
Insertion Sort List

Given the head of a singly linked list, sort the list using insertion sort,
and return the sorted list's head.

The steps of the insertion sort algorithm:

    Insertion sort iterates, consuming one input element each repetition
    and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data,
    finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm.
The partially sorted list (black) initially contains only the first element in the list.
One element (red) is removed from the input data and inserted in-place into the sorted
list with each iteration.

Example 1:

4 -> 2 -> 1 -> 3
1 -> 2 -> 3 -> 4

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

-1 -> 5 -> 3 -> 4 -> 0
-1 -> 0 -> 3 -> 4 -> 5

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:

    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def push(self, root: ListNode, val):
        node = ListNode(val=val, next=root)
        root = node
        return root

    def sorted_insert(self, root, node):
        if root is None or root.val >= node.val:
            node.next = root
            root = node
        else:
            current_node = root
            while current_node.next is not None and current_node.next.val < node.val:
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
        return root

    def insertionSortList(self, head: ListNode) -> ListNode:
        nodes = None
        current_node = head
        while current_node is not None:
            next_node = current_node.next
            nodes = self.sorted_insert(nodes, current_node)
            current_node = next_node
        root = nodes
        return root

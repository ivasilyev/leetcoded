"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # Recursive
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val < list2.val:
            node = list1
            node.next = self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next = self.mergeTwoLists(list1, list2.next)
        return node

    def mergeTwoLists2(self, list1: ListNode, list2: ListNode):
        # Iterative
        root = ListNode()
        node = root
        while True:
            if list1 is None:
                node.next = list2
                break
            elif list2 is None:
                node.next = list1
                break
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        return root.next


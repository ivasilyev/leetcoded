"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

1 - 2 - 2 - 1

Input: head = [1,2,2,1]
Output: true

Example 2:

1 - 2

Input: head = [1,2]
Output: false

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode):
        current_node = head
        length = 0
        values = list()
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
            length += 1
        current_node = head
        for value in values[::-1]:
            if value != current_node.val:
                return False
            current_node = current_node.next
        return True

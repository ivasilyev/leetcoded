"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

1 - 2 - 3 - 4 - 5 -> 1 - 2 - 3 - 5

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if head is None:
            return
        node = head
        size = 0
        while node is not None:
            node = node.next
            size += 1

        size -= n
        if size == 0:
            node = head.next
            head.next = None
            del head
            return node

        current_node = head
        previous_node = None
        while size > 0:
            previous_node = current_node
            current_node = current_node.next
            size -= 1

        previous_node.next = current_node.next
        current_node.next = None
        del current_node
        return head


        if number == 0:
            return head.next

        node_1 = head
        while number > 0:
            node_1 = node_1.next
            number -= 1
        node_2 = node_1.next
        if node_2 is None or node_2.next is None:
            node_1.next = None
        else:
            node_1.next = node_2.next
        return head





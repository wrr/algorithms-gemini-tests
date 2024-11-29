
"""
Reverse a singly linked list. For example:

1 --> 2 --> 3 --> 4
After reverse:
4 --> 3 --> 2 --> 1
"""
#
# Iterative solution
# T(n)- O(n)
#

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


#
# Recursive solution
# T(n)- O(n)
#
def reverse_list_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    p = head.next
    head.next = None
    revrest = reverse_list_recursive(p)
    p.next = head
    return revrest

import unittest


class ReverseGeminiTest(unittest.TestCase):
    def test_gemini_reverse_list_empty_list(self):
        self.assertEqual(reverse_list(None), None)

    def test_gemini_reverse_list_single_node(self):
        head = Node(1)
        self.assertEqual(reverse_list(head).val, 1)

    def test_gemini_reverse_list_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        reversed_head = reverse_list(head)
        self.assertEqual(reversed_head.val, 4)
        self.assertEqual(reversed_head.next.val, 3)
        self.assertEqual(reversed_head.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.val, 1)

    def test_gemini_reverse_list_recursive_empty_list(self):
        self.assertEqual(reverse_list_recursive(None), None)

    def test_gemini_reverse_list_recursive_single_node(self):
        head = Node(1)
        self.assertEqual(reverse_list_recursive(head).val, 1)

    def test_gemini_reverse_list_recursive_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        reversed_head = reverse_list_recursive(head)
        self.assertEqual(reversed_head.val, 4)
        self.assertEqual(reversed_head.next.val, 3)
        self.assertEqual(reversed_head.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.val, 1)


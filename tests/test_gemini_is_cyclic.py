
import unittest
from algorithms.linkedlist.is_cyclic import Node, is_cyclic


class IsCyclicGeminiTest(unittest.TestCase):
    def test_gemini_is_cyclic_empty_list(self):
        self.assertFalse(is_cyclic(None))

    def test_gemini_is_cyclic_single_node(self):
        head = Node(1)
        self.assertFalse(is_cyclic(head))

    def test_gemini_is_cyclic_no_cycle(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        self.assertFalse(is_cyclic(head))

    def test_gemini_is_cyclic_cycle_exists(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = head.next
        self.assertTrue(is_cyclic(head))

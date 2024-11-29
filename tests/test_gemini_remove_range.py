
"""
Given a linked list, remove_range function accepts a starting and ending index
as parameters and removes the elements at those indexes (inclusive) from the list

For example:
List: [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
remove_range(list, 3, 8);
List becomes: [8, 13, 17, 23, 0, 92]

legal range of the list (0 < start index < end index < size of list).
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_range(head, start, end):
    assert(start <= end)
    # Case: remove node at head
    if start == 0:
        for i in range(0, end+1):
            if head != None:
                head = head.next
    else:
        current = head
        # Move pointer to start position
        for i in range(0,start-1):
            current = current.next
        # Remove data until the end
        for i in range(0, end-start + 1):
            if current != None and current.next != None:
                current.next = current.next.next
    return head

import unittest


class RemoveRangeGeminiTest(unittest.TestCase):
    def test_gemini_remove_range_middle_case(self):
        head = Node(8)
        head.next = Node(13)
        head.next.next = Node(17)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(9)
        head.next.next.next.next.next = Node(12)
        head.next.next.next.next.next.next = Node(98)
        head.next.next.next.next.next.next.next = Node(41)
        head.next.next.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next.next.next = Node(23)
        head.next.next.next.next.next.next.next.next.next.next = Node(0)
        head.next.next.next.next.next.next.next.next.next.next.next = Node(92)
        head = remove_range(head, 3, 8)
        current = head
        expected_data = [8, 13, 17, 23, 0, 92]
        for i in range(len(expected_data)):
            self.assertEqual(current.data, expected_data[i])
            current = current.next

    def test_gemini_remove_range_remove_head(self):
        head = Node(8)
        head.next = Node(13)
        head.next.next = Node(17)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(9)
        head.next.next.next.next.next = Node(12)
        head.next.next.next.next.next.next = Node(98)
        head.next.next.next.next.next.next.next = Node(41)
        head.next.next.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next.next.next = Node(23)
        head.next.next.next.next.next.next.next.next.next.next = Node(0)
        head.next.next.next.next.next.next.next.next.next.next.next = Node(92)
        head = remove_range(head, 0, 2)
        current = head
        expected_data = [4, 9, 12, 98, 41, 7, 23, 0, 92]
        for i in range(len(expected_data)):
            self.assertEqual(current.data, expected_data[i])
            current = current.next


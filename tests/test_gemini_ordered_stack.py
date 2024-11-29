
# The stack remains always ordered such that the highest value
# is at the top and the lowest at the bottom


class OrderedStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_t(self, item):
        self.items.append(item)

    # push method to maintain order when pushing new elements
    def push(self, item):
        temp_stack = OrderedStack()
        if self.is_empty() or item > self.peek():
            self.push_t(item)
        else:
            while item < self.peek() and not self.is_empty():
                temp_stack.push_t(self.pop())
            self.push_t(item)
            while not temp_stack.is_empty():
                self.push_t(temp_stack.pop())

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

import unittest


class OrderedStackGeminiTest(unittest.TestCase):
    def test_gemini_ordered_stack_push_and_pop(self):
        stack = OrderedStack()
        stack.push(1)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_gemini_ordered_stack_peek(self):
        stack = OrderedStack()
        stack.push(1)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        self.assertEqual(stack.peek(), 2)

    def test_gemini_ordered_stack_is_empty(self):
        stack = OrderedStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_gemini_ordered_stack_size(self):
        stack = OrderedStack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

    def test_gemini_ordered_stack_pop_from_empty_stack(self):
        stack = OrderedStack()
        with self.assertRaises(IndexError):
            stack.pop()


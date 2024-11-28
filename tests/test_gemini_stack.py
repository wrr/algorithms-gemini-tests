import unittest
from algorithms.stack.stack import ArrayStack, LinkedListStack


class StackGeminiTest(unittest.TestCase):
    def test_gemini_array_stack_push(self):
        stack = ArrayStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, len(stack))

    def test_gemini_array_stack_pop_empty(self):
        stack = ArrayStack()
        with self.assertRaisesRegex(IndexError, "Stack is empty"):
            stack.pop()

    def test_gemini_array_stack_peek_empty(self):
        stack = ArrayStack()
        with self.assertRaisesRegex(IndexError, "Stack is empty"):
            stack.peek()

    def test_gemini_linked_list_stack_push(self):
        stack = LinkedListStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, len(stack))

    def test_gemini_linked_list_stack_pop_empty(self):
        stack = LinkedListStack()
        with self.assertRaisesRegex(IndexError, "Stack is empty"):
            stack.pop()

    def test_gemini_linked_list_stack_peek_empty(self):
        stack = LinkedListStack()
        with self.assertRaisesRegex(IndexError, "Stack is empty"):
            stack.peek()


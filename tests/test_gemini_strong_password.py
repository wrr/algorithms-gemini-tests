
import unittest
from algorithms.strings.strong_password import strong_password


class StrongPasswordGeminiTest(unittest.TestCase):
    def test_gemini_strong_password(self):
        self.assertEqual(3, strong_password(3, "Ab1"))
        self.assertEqual(1, strong_password(11, "#Algorithms"))
        self.assertEqual(1, strong_password(5, "jnh!Y"))
        self.assertEqual(1, strong_password(5, "JNH!7"))
        self.assertEqual(5, strong_password(1, "*"))
        self.assertEqual(0, strong_password(6, "2@u9aP"))

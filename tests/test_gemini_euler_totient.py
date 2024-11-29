
import unittest
from algorithms.maths.euler_totient import euler_totient


class TestEulerTotientGeminiTest(unittest.TestCase):
    def test_gemini_euler_totient_small_numbers(self):
        self.assertEqual(1, euler_totient(1))
        self.assertEqual(1, euler_totient(2))
        self.assertEqual(2, euler_totient(3))
        self.assertEqual(2, euler_totient(4))
        self.assertEqual(4, euler_totient(5))
        self.assertEqual(2, euler_totient(6))
        self.assertEqual(6, euler_totient(7))
        self.assertEqual(4, euler_totient(8))
        self.assertEqual(6, euler_totient(9))
        self.assertEqual(4, euler_totient(10))

    def test_gemini_euler_totient_prime_numbers(self):
        self.assertEqual(12, euler_totient(13))
        self.assertEqual(16, euler_totient(17))
        self.assertEqual(18, euler_totient(19))

    def test_gemini_euler_totient_large_number(self):
        self.assertEqual(2000, euler_totient(5000))

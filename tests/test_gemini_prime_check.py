
import unittest
from algorithms.maths.prime_check import prime_check


class TestPrimeCheckGeminiTest(unittest.TestCase):
    def test_gemini_prime_check_small_primes(self):
        self.assertTrue(prime_check(2))
        self.assertTrue(prime_check(3))
        self.assertTrue(prime_check(5))
        self.assertTrue(prime_check(7))
        self.assertTrue(prime_check(11))
        self.assertTrue(prime_check(13))

    def test_gemini_prime_check_small_composites(self):
        self.assertFalse(prime_check(1))
        self.assertFalse(prime_check(4))
        self.assertFalse(prime_check(6))
        self.assertFalse(prime_check(8))
        self.assertFalse(prime_check(9))
        self.assertFalse(prime_check(10))

    def test_gemini_prime_check_large_prime(self):
        self.assertTrue(prime_check(999983))

    def test_gemini_prime_check_large_composite(self):
        self.assertFalse(prime_check(1000000))

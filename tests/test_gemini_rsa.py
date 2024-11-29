
import unittest
from algorithms.maths.rsa import generate_key, encrypt, decrypt


class RSAGeminiTest(unittest.TestCase):
    def test_gemini_rsa_encrypt_decrypt(self):
        n, e, d = generate_key(16)
        data = 20
        encrypted = encrypt(data, e, n)
        decrypted = decrypt(encrypted, d, n)
        self.assertEqual(data, decrypted)


import unittest
from algorithms.strings.validate_coordinates import is_valid_coordinates_0, is_valid_coordinates_1, is_valid_coordinates_regular_expression


class ValidateCoordinatesGeminiTest(unittest.TestCase):
    def test_gemini_is_valid_coordinates_0_valid(self):
        self.assertTrue(is_valid_coordinates_0("-23, 25"))
        self.assertTrue(is_valid_coordinates_0("43.91343345, 143"))
        self.assertTrue(is_valid_coordinates_0("4, -3"))

    def test_gemini_is_valid_coordinates_0_invalid(self):
        self.assertFalse(is_valid_coordinates_0("23.234, - 23.4234"))
        self.assertFalse(is_valid_coordinates_0("N23.43345, E32.6457"))
        self.assertFalse(is_valid_coordinates_0("6.325624, 43.34345.345"))
        self.assertFalse(is_valid_coordinates_0("0, 1,2"))

    def test_gemini_is_valid_coordinates_1_valid(self):
        self.assertTrue(is_valid_coordinates_1("-23, 25"))
        self.assertTrue(is_valid_coordinates_1("43.91343345, 143"))
        self.assertTrue(is_valid_coordinates_1("4, -3"))

    def test_gemini_is_valid_coordinates_1_invalid(self):
        self.assertFalse(is_valid_coordinates_1("23.234, - 23.4234"))
        self.assertFalse(is_valid_coordinates_1("N23.43345, E32.6457"))
        self.assertFalse(is_valid_coordinates_1("6.325624, 43.34345.345"))
        self.assertFalse(is_valid_coordinates_1("0, 1,2"))

    def test_gemini_is_valid_coordinates_regular_expression_valid(self):
        self.assertTrue(is_valid_coordinates_regular_expression("-23, 25"))
        self.assertTrue(is_valid_coordinates_regular_expression("43.91343345, 143"))
        self.assertTrue(is_valid_coordinates_regular_expression("4, -3"))

    def test_gemini_is_valid_coordinates_regular_expression_invalid(self):
        self.assertFalse(is_valid_coordinates_regular_expression("23.234, - 23.4234"))
        self.assertFalse(is_valid_coordinates_regular_expression("N23.43345, E32.6457"))
        self.assertFalse(is_valid_coordinates_regular_expression("6.325624, 43.34345.345"))
        self.assertFalse(is_valid_coordinates_regular_expression("0, 1,2"))


"""
Calculate cosine similarity between given two 1d list.
Two list must have the same length.

Example:
cosine_similarity([1, 1, 1], [1, 2, -1])  # output : 0.47140452079103173
"""
import math


def _l2_distance(vec):
    """
    Calculate l2 distance from two given vectors.
    """
    norm = 0.
    for element in vec:
        norm += element * element
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between given two vectors
    :type vec1: list
    :type vec2: list
    """
    if len(vec1) != len(vec2):
        raise ValueError("The two vectors must be the same length. Got shape " + str(len(vec1))
                        + " and " + str(len(vec2)))

    norm_a = _l2_distance(vec1)
    norm_b = _l2_distance(vec2)

    similarity = 0.

    # Calculate the dot product of two vectors
    for vec1_element, vec2_element in zip(vec1, vec2):
        similarity += vec1_element * vec2_element

    similarity /= (norm_a * norm_b)

    return similarity

import unittest


class CosineSimilarityGeminiTest(unittest.TestCase):
    def test_gemini_cosine_similarity_same_vector(self):
        vec1 = [1, 2, 3]
        self.assertEqual(cosine_similarity(vec1, vec1), 1.0)

    def test_gemini_cosine_similarity_different_vectors(self):
        vec1 = [1, 1, 1]
        vec2 = [1, 2, -1]
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.47140452079103173)

    def test_gemini_cosine_similarity_different_length(self):
        vec1 = [1, 2, 3]
        vec2 = [1, 2]
        with self.assertRaises(ValueError):
            cosine_similarity(vec1, vec2)


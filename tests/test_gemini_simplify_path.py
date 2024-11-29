
"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

Reference: https://leetcode.com/problems/simplify-path/description/
"""

import os
def simplify_path_v1(path):
    return os.path.abspath(path)

def simplify_path_v2(path):
    stack, tokens = [], path.split("/")
    for token in tokens:
        if token == ".." and stack:
            stack.pop()
        elif token != ".." and token != "." and token:
            stack.append(token)
    return "/" + "/".join(stack)

import unittest


class SimplifyPathGeminiTest(unittest.TestCase):
    def test_gemini_simplify_path_v1_root_path(self):
        self.assertEqual(simplify_path_v1("/"), "/")

    def test_gemini_simplify_path_v1_home_path(self):
        self.assertEqual(simplify_path_v1("/home/"), "/home")

    def test_gemini_simplify_path_v1_complex_path(self):
        self.assertEqual(simplify_path_v1("/a/./b/../../c/"), "/c")

    def test_gemini_simplify_path_v1_parent_directory_path(self):
        self.assertEqual(simplify_path_v1("/../"), "/")

    def test_gemini_simplify_path_v1_multiple_slashes_path(self):
        self.assertEqual(simplify_path_v1("/home//foo/"), "/home/foo")

    def test_gemini_simplify_path_v2_root_path(self):
        self.assertEqual(simplify_path_v2("/"), "/")

    def test_gemini_simplify_path_v2_home_path(self):
        self.assertEqual(simplify_path_v2("/home/"), "/home")

    def test_gemini_simplify_path_v2_complex_path(self):
        self.assertEqual(simplify_path_v2("/a/./b/../../c/"), "/c")

    def test_gemini_simplify_path_v2_parent_directory_path(self):
        self.assertEqual(simplify_path_v2("/../"), "/")

    def test_gemini_simplify_path_v2_multiple_slashes_path(self):
        self.assertEqual(simplify_path_v2("/home//foo/"), "/home/foo")


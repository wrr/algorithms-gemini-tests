
"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.

eg: for given string -> "appletablet"
"apple", "tablet"
"applet", "able", "t"
"apple", "table", "t"
"app", "let", "able", "t"

"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1
"""

count = 0


def make_sentence(str_piece, dictionaries):
    global count
    if len(str_piece) == 0:
        return True
    for i in range(1, len(str_piece) + 1):
        prefix, suffix = str_piece[0:i], str_piece[i:]
        if prefix in dictionaries:
            if suffix in dictionaries or make_sentence(suffix, dictionaries):
                count += 1
    return False

import unittest


class MakeSentenceGeminiTest(unittest.TestCase):
    def test_gemini_make_sentence_multiple_sentences(self):
        global count
        count = 0
        dictionaries = ["", "app", "let", "t", "apple", "applet"]
        word = "applet"
        make_sentence(word, dictionaries)
        self.assertEqual(count, 3)

    def test_gemini_make_sentence_single_sentence(self):
        global count
        count = 0
        dictionaries = ["thing"]
        word = "thing"
        make_sentence(word, dictionaries)
        self.assertEqual(count, 1)

    def test_gemini_make_sentence_no_sentence(self):
        global count
        count = 0
        dictionaries = ["apple", "pie"]
        word = "appletablet"
        make_sentence(word, dictionaries)
        self.assertEqual(count, 0)

    def test_gemini_make_sentence_empty_string(self):
        global count
        count = 0
        dictionaries = ["apple", "pie"]
        word = ""
        make_sentence(word, dictionaries)
        self.assertEqual(count, 0)


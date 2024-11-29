
def DFA(transitions, start, final, string):

    num = len(string)
    num_final = len(final)
    cur = start

    for i in range(num):

        if transitions[cur][string[i]] is None:
            return False
        else:
            cur = transitions[cur][string[i]]

    for i in range(num_final):
        if cur == final[i]:
            return True
    return False

import unittest


class DFAGeminiTest(unittest.TestCase):
    def test_gemini_dfa_accepting_string(self):
        transitions = {
            'a': {'0': 'a', '1': 'b'},
            'b': {'0': 'b', '1': 'a'}
        }
        start = 'a'
        final = ['a']
        string = '010100'
        self.assertTrue(DFA(transitions, start, final, string))

    def test_gemini_dfa_rejecting_string(self):
        transitions = {
            'a': {'0': 'a', '1': 'b'},
            'b': {'0': 'b', '1': 'a'}
        }
        start = 'a'
        final = ['a']
        string = '010101'
        self.assertFalse(DFA(transitions, start, final, string))

    def test_gemini_dfa_invalid_input(self):
        transitions = {
            'a': {'0': 'a', '1': 'b'},
            'b': {'0': 'b', '1': 'a'}
        }
        start = 'a'
        final = ['a']
        string = '012010'
        self.assertFalse(DFA(transitions, start, final, string))


import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        print('test_lowercase_identifier')
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        print('test_lower_upper_id')
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_mixed_id(self):
        print('test_mixed_id')
        self.assertTrue(TestLexer.test("aAsVN3", "aAsVN,3,<EOF>", 103))

    def test_integer(self):
        """test integers"""
        print('test_integer')
        self.assertTrue(TestLexer.test("123a123", "123,a,123,<EOF>", 104))

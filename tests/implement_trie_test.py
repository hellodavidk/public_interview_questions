from __future__ import annotations
import unittest

from solutions.implement_trie_solution import Trie


class ImplementTrieTest(unittest.TestCase):
    def setUp(self: ImplementTrieTest) -> None:
        pass

    def tearDown(self: ImplementTrieTest) -> None:
        pass

    def test_example(self: ImplementTrieTest) -> None:
        trie = Trie()
        trie.insert('apple')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))
        trie.insert('app')
        self.assertTrue(trie.search('app'))

    def test_multiple_words(self: ImplementTrieTest) -> None:
        trie = Trie()
        trie.insert('apple')
        trie.insert('berry')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))
        self.assertTrue(trie.search('berry'))
        self.assertFalse(trie.search('berr'))
        self.assertTrue(trie.startsWith('berr'))

    def test_multiple_words_with_same_prefix(self: ImplementTrieTest) -> None:
        trie = Trie()
        trie.insert('apple')
        trie.insert('application')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))
        self.assertTrue(trie.search('application'))
        self.assertFalse(trie.search('appli'))
        self.assertTrue(trie.startsWith('appli'))


if __name__ == '__main__':
    unittest.main()

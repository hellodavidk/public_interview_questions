'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''
from __future__ import annotations


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Trie:

    def __init__(self: Trie) -> None:
        """
        Initialize your data structure here.
        """
        pass

    def insert(self: Trie, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pass

    def search(self: Trie, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass

    def startsWith(self: Trie, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """
        pass


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.word = False
        
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curRoot = self.root
        for letter in word:
            if letter not in curRoot.children:
                curRoot.children[letter] = TrieNode()
            curRoot = curRoot.children[letter]
        curRoot.word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curRoot = self.root
        for letter in word:
            if letter not in curRoot.children:
                return False
            curRoot = curRoot.children[letter]
        return curRoot.word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curRoot = self.root
        for letter in prefix:
            if letter not in curRoot.children:
                return False
            curRoot = curRoot.children[letter]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

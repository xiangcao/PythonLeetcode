class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for l in word:
            if l not in root.children:
                root.children[l] = TrieNode()
            root = root.children[l]
        root.word = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        queue=[root]
        for l in word:
            next=[]
            found = False
            while queue:
                root = queue.pop()
                if l == '.':
                    for child in root.children.values():
                        found = True
                        next.append(child)
                elif l in root.children:
                        found = True
                        next.append(root.children[l])
            if not found:
                return False
            queue = next
        
        for node in queue:
            if node.word:
                return True
        return False
                    
                    
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

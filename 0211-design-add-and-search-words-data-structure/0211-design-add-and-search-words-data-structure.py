class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        cur = self.root
        for w in word:
            if not cur.children[(ord(w) - ord('a'))]:
                cur.children[ord(w) - ord('a')] = TrieNode()
            cur = cur.children[ord(w) - ord('a')]
            
        cur.is_end = True
        
        
    def search(self, cur: TrieNode, word: str, i: int) -> bool:
        
        if i >= len(word) or not cur:
            if cur and cur.is_end:
                return True
            return False
        
        if word[i] == '.':
            for node in cur.children:
                if self.search(node, word, i + 1):
                    return True
            return False
            
        
        if not cur or not cur.children[ord(word[i]) - ord('a')]:
            return False
        
        return True and self.search(cur.children[ord(word[i]) - ord('a')], word, i + 1)
        

class WordDictionary:

    def __init__(self):
        self._dict = Trie()
        

    def addWord(self, word: str) -> None:
        self._dict.insert(word)
        

    def search(self, word: str) -> bool:
        return self._dict.search(self._dict.root, word, 0)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
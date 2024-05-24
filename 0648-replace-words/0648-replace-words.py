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
        
        
    def search(self, word: str) -> bool:
        
        cur = self.root
        idx = 0
        
        for w in word:
            if not cur.children[ord(w) - ord('a')]:
                
                if idx == 0 or not cur.is_end:
                    return len(word)
                return idx
            
            cur = cur.children[ord(w) - ord('a')]
            idx += 1
            
            if cur.is_end:
                return idx
            
        
        if cur.is_end:
            return idx
        return len(word)
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        _dict = Trie()
        
        for word in dictionary:
            _dict.insert(word)
            
         
        words = sentence.split()
        
        for i, word in enumerate(words):
            words[i] = word[0:_dict.search(word)]
        
        
        return " ".join(words)
            
            
            
            
            
            
            
        
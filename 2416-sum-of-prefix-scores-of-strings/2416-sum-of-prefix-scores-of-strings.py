class TrieNode:
    def __init__(self):
        self.is_end = False
        self.count = 0
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
            cur.count += 1
            
        cur.is_end = True
        
        
    def search(self, word: str) -> bool:
        
        cur = self.root
        count = 0
        for w in word:
#             if not cur.children[ord(w) - ord('a')]:
#                 return count
            
            
            cur = cur.children[ord(w) - ord('a')]
            count += cur.count
        
        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        
        ans = []
        for word in words:
            ans.append(trie.search(word))
        
        return ans
            
        
        
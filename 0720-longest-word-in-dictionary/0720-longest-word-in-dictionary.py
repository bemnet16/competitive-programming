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
        for w in word:
            if not cur.children[ord(w) - ord('a')]:
                return False
            cur = cur.children[ord(w) - ord('a')]
        
        if cur.is_end:
            return True
        return False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        letters = [chr(i) for i in range(97, 123)]
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        queue = []
        cur = trie.root.children
        for i, child in enumerate(cur):
            if child and child.is_end:
                queue.append((child, letters[i]))
            
        ans = ""
        if queue:
            ans = queue[0][1]
            
        while queue:
            
            nx_que = []
            
            for n in queue:
                cur, word = n
                
                for i, child in enumerate(cur.children):
                    if child and child.is_end:
                        nx_que.append((child, word + letters[i]))
                
            
            if nx_que:
                queue = nx_que
                ans = nx_que[0][1]
            
            else:
                return ans
        
        
        return ans
        

        
        
        
        
        
        
        
        
        
        
        
        
        
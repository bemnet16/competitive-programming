class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        hashes = {}
        used = set()
        
        for pat, word in zip(pattern, s):
            
            if pat in hashes and hashes[pat] != word:
                return False
            
            elif pat not in hashes and word in used:
                return False
            
            hashes[pat] = word
            used.add(word)
        
        
        return True
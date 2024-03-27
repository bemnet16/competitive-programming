class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        charmap = defaultdict(str)
        reserved = set()
        
        for i in range(len(s)):
            
            if s[i] not in charmap and t[i] not in reserved:
                charmap[s[i]] = t[i]
                reserved.add(t[i])
          
        
        chars = []
        
        for c in s:
            chars.append(charmap[c])
        
        return "".join(chars) == t
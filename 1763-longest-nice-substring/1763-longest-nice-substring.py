class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            
            lowers = 0
            uppers = 0
            
            for j in range(i, len(s)):
                
                char_ord = ord(s[j])
                
                if char_ord < 97:
                    uppers |= 1 << (char_ord - 65)
                
                else:
                    lowers |= 1 << (char_ord - 97)
                
                
                if (lowers == uppers) and ((j - i + 1) > (end - start)):
                    start = i
                    end = j + 1
        
        
        
        return s[start:end]
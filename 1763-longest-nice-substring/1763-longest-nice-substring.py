class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def div(strs):
            
            if not strs or len(strs) < 2:
                return ""
            
            letrs = set(strs)
            
            for i, char in enumerate(strs):
                
                if not (char.lower() in letrs and char.upper() in letrs):
                    
                    strs_1 = div(strs[:i])
                    strs_2 = div(strs[i + 1:])
                    
                    if len(strs_1) >= len(strs_2):
                        return strs_1
                    return strs_2
                    
            return strs
                        
                        
        return div(s)

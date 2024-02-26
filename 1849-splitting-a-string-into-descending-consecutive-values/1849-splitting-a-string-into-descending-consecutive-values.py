class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(idx, pre_val):
            if idx == len(s):
                return True
            
            for i in range(idx, len(s)):
                cur = int(s[idx:(i + 1)])
                if (cur + 1) == pre_val and backtrack(i + 1, cur):
                    return True
            return False
                
        
        
        for i in range(len(s) - 1):
            cur = int(s[:(i + 1)])
            
            if cur == 0:
                continue
                
            if backtrack(i + 1, cur):
                return True
        
        return False
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        while n:
            
            if n & 1 == (n >> 1) &  1:
                return False
            n = n >> 1
    
        return True
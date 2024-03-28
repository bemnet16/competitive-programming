class Solution:
    def isUgly(self, n: int) -> bool:
        
        while n >= 1:
            
            if n % 2 == 0:
                n //=2
            
            elif n % 3 == 0:
                n //= 3
            
            elif n % 5 == 0:
                n //=5
            
            elif n == 1:
                return True
            
            else:
                return False
        
        
        return False
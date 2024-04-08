import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        for i in range(1, math.ceil(math.sqrt(n))):
            if  n % i == 0:
                k -= 1
            
            if k == 0:
                return i
        
        for i in range(int(math.sqrt(n)), 0, -1):
            if (n % (n // i)) == 0:
                k -= 1
            
            if k == 0:
                return n // i
        
        return -1
    

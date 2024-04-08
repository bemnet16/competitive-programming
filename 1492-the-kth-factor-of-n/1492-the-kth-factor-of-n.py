import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        for i in range(1, int(math.sqrt(n)) + 1):
            
            if not (n % i):
                k -= 1
            
            if not k:
                return i
        
        for i in range(int(math.sqrt(n)), 0, -1):
            
            if not (n % (n // i)):
                k -= 1
            
            if not k:
                return n // i
        
        return -1
    
    import math 
class Solution: 
    def kthFactor(self, n: int, k: int) -> int:
        root = math.sqrt(n)
        i = 1
        while i < root:
            if n % i == 0: 
                k -= 1
            if k == 0: 
                return i
            i += 1
        for j in range(int(root), 0, -1):
            if n % (n//j) == 0: 
                k -= 1
            if k == 0: 
                return n//j
        return -1   
                
            
        
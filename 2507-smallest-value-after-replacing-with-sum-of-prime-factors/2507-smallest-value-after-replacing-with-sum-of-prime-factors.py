import math

class Solution:
    def smallestValue(self, n: int) -> int:
        
        for _ in range(10000):
            
            cnt = 0
            tot = 0
            cur = n
            
            for i in range(2, math.ceil(math.sqrt(n)) + 1):
                
                while n % i == 0 and n > 1:
                    cnt += 1
                    tot += i
                    n //= i
            
            if n > 1:
                tot += n
                cnt += 1
                
            if cnt < 2:
                return cur
            
            n = tot
            cur = n
                
        return n
            
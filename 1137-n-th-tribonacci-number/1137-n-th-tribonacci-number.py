class Solution:
    def tribonacci(self, n: int) -> int:
        
        known_trib = {0:0, 1:1, 2:1}
        
        def triBon(n):
        
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1
            
            if (n - 1) not in known_trib:
                t3 = triBon(n - 1)
                known_trib[n - 1] = t3
            else:
                t3 = known_trib[n - 1]
                
            if (n - 2) not in known_trib:
                t2 = triBon(n - 2)
                known_trib[n - 2] = t2
            else:
                t2 = known_trib[n - 2]
            
            if (n - 3) not in known_trib:
                t1 = triBon(n - 3)
                known_trib[n - 3] = t1
            else:
                t1 = known_trib[n - 3]
            
            
            return t1 + t2 + t3
        
        return triBon(n)
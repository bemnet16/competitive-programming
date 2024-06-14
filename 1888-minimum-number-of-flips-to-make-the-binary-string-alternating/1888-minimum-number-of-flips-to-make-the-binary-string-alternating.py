class Solution:
    def minFlips(self, s: str) -> int:
        
        s0 = '0'
        s1 = '1'
        
        ts0 = 0
        ts1 = 0
        
        ans = len(s)
        
        for c in s:
            if c == '1':
                if s1 == '1':
                    ts0 += 1
                else:
                    ts1 += 1
            else:
                if s0 == '0':
                    ts1 += 1
                else:
                    ts0 += 1
                    
            s0, s1 = s1, s0
            
        n0 = '0'
        n1 = '1'
            
        for c in s:
            if c == '1':
                if s1 == '1':
                    ts0 += 1
                else:
                    ts1 += 1
                
                if n1 == '1':
                    ts0 -= 1
                else:
                    ts1 -= 1
                
            else:
                if s0 == '0':
                    ts1 += 1
                else:
                    ts0 += 1
                
                if n0 == '0':
                    ts1 -= 1
                else:
                    ts0 -= 1
                    
            ans = min(ans, ts0, ts1)
            s0, s1 = s1, s0
            n0, n1 = n1, n0
            
            
        
        
        return min(ans, ts0, ts1)
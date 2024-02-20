class Solution:
    def climbStairs(self, n: int) -> int:
        
        d = {1:1, 2:2}
        
        def ans(n):
            
            if n == 1: return 1
            if n == 2: return 2
            
            if (n - 1) not in d:
                fl = ans(n - 1)
                d[n - 1] = fl
            else:
                fl = d[n - 1]
            
            if (n - 2) not in d:
                fr = ans(n - 2)
                d[n - 2] = fr
            else:
                fr = d[n - 2]
            
            return fl + fr
        
        return ans(n)
        
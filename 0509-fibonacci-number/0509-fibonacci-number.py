class Solution:
    def fib(self, n: int) -> int:
        
        d = {0:0, 1:1}
        
        if n <= 1: return n
        
        if n - 1 not in d:
            fl = self.fib(n - 1)
        else:
            fl = d[n - 1]
        
        if n - 2 not in d:
            fr = self.fib(n - 2)
        else:
            fr = d[n - 2]
        
        return fl + fr
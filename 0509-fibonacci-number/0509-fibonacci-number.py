class Solution:
    def fib(self, n: int) -> int:
        
        d = {0:0, 1:1}
        
        def f(n):
            if n <= 1: return n

            if n - 1 not in d:
                fl = self.fib(n - 1)
                d[n - 1] = fl
            else:
                fl = d[n - 1]

            if n - 2 not in d:
                fr = self.fib(n - 2)
                d[n - 2] = fr
            else:
                fr = d[n - 2]

            return fl + fr
        
        return f(n)
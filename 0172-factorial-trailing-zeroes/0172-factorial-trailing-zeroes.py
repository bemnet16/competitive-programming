class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n == 0: return 0
        
        def factorial(n):
            
            if n == 1: return 1
            
            return n * factorial(n - 1)
        
        
        
        n_factorial = factorial(n)
        answer = 0
        
        while n_factorial % 10 == 0:
            
            answer += 1
            n_factorial //= 10
        
        return answer
            
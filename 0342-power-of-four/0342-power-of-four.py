class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False

        def isPower(n):
            
            if n == 1:
                return True
            if n < 1 or (n % 4 != 0):
                return False
            
            return isPower(n / 4)
        
        return isPower(n)

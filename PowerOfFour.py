class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        isPower = False
        if n > 0:
            if bin(n).count('1') == 1:
                isPower = ((n - 1) % 3) == 0
                
        return isPower

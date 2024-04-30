class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 1
        
        while n > 1:
            
            if n & 1:
                count += 1
            
            n = n >> 1
        
        
        return count
        
        
        
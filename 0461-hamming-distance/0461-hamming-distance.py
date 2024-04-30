class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        dis = 0
        val = x ^ y
        
        while val:
            
            dis += 1
            val = val & (val - 1)
        
        return dis
        
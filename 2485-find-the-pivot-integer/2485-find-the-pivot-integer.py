class Solution:
    def pivotInteger(self, n: int) -> int:
        
        tot = n * (n + 1) / 2
        pre = 0
        
        for i in range(1, n + 1):
            
            pre += i
            
            if pre - i == tot - pre:
                return i
        
        
        return -1
            
            
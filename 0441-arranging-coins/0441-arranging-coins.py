class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        rows = 0
        pre = 1
        
        while n - pre >= 0:
            rows += 1
            n -= pre
            pre += 1
        
        
        return rows
            
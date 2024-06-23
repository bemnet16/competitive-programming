class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        symbol = 1
        
        for row in range(n, 1, -1):
            total_ele = 1 << (row - 1)
            half_ele = total_ele // 2
            
            if k > half_ele:
                symbol = 1 - symbol
                k -= half_ele
        
        if symbol == 1:
            return 0
        return 1
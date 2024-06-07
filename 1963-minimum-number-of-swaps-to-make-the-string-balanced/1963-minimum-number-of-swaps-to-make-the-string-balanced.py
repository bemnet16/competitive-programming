class Solution:
    def minSwaps(self, s: str) -> int:
        
        diff = 0
        swaps = 0
        
        for brace in s:
            
            if brace == ']':
                diff += 1
                swaps = max(swaps, diff)
                
            else:
                diff -= 1
        
        return (swaps + 1) // 2
        
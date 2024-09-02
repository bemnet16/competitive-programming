class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        k %= sum(chalk)
        
        for i, cha in enumerate(chalk):
            if cha > k:
                return i
            
            k -= cha
        
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        
        m = len(potions)
        potions.sort()
        successful = []
        
        
        for spell in spells:
            
            min_potion = ceil(success / spell)
            pairs = m - bisect_left(potions, min_potion)
            successful.append(pairs)
        
        
        
        return successful

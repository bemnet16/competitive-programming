class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        a_tot = sum(aliceSizes)
        b_tot = sum(bobSizes)
        set_a = set(aliceSizes)
        set_b = set(bobSizes)
        diff = (a_tot - b_tot)//2
        res = [[c + diff,c] for c in set_b if (diff + c) in set_a]
        return res[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
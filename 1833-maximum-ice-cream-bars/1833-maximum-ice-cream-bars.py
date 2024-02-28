class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        num_ice_cream = 0
        
        for cost in costs:
            
            if (coins - cost) >= 0:
                num_ice_cream += 1
                coins -= cost
            else:
                return num_ice_cream
        
        
        return num_ice_cream
            
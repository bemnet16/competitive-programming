class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        steps = 0
        
        can = capacity
        for i, plant in enumerate(plants):
            if can - plant < 0:
                steps += (i * 2 + 1) 
                can = capacity - plant
            else:
                steps += 1
                can -= plant
        
        
        return steps
                
            
        
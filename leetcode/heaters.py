class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        
        def validRadius(radius):

            houses_pointer = 0
            heaters_pointer = 0
            
            while houses_pointer < len(houses) and heaters_pointer < len(heaters):
                
                # check current house can be coverd by this radius, if it is go to the next house
                # if not try to the next heater to check if still the house is within the radius
                
                if abs(houses[houses_pointer] - heaters[heaters_pointer]) <= radius:
                    houses_pointer += 1
                
                else:
                    heaters_pointer += 1
            
            # the pointer must be equal to length of houes if all houses can be coverd by this radius
            return houses_pointer == len(houses)
                
                
            
        min_house = min(houses)
        max_house = max(houses)
        
        min_heater = min(heaters)
        max_heater = max(heaters)
        
        # take minimum possible and maximum possible radius as low and high respectively
        low = min(abs(min_house - min_heater), abs(max_heater - max_heater))
        high = max(abs(max_house - min_heater), abs(max_heater - min_house))
        

        while low <= high:
            
            mid = low + (high - low) // 2
            
            if validRadius(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return low
            
            
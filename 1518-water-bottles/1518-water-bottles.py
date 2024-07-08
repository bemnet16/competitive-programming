class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        empty = numBottles
        ans = numBottles
        
        while empty >= numExchange:
            
            ans += empty // numExchange
            empty = empty // numExchange + empty % numExchange
            
        
        return ans
    
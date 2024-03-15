class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            
            count_hour = 0
            
            for bananas in piles:
                count_hour += ceil(bananas / k)
            
            
            return count_hour <= h
        
        
        low = 1
        high = max(piles)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return low
        
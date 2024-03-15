class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            mid_sqr = mid * mid
            
            if mid_sqr == x:
                return mid
            
            elif mid_sqr > x:
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return high
        
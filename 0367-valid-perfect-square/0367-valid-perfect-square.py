class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        low = 0
        high = num
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            sqr = mid * mid
            
            if sqr < num:
                low = mid + 1
            
            elif sqr > num:
                high = mid - 1
            
            else:
                return True
        
        
        return False
        
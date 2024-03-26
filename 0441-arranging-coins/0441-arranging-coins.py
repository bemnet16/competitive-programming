class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        low = 0
        high = n
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            s = mid * (mid + 1) // 2
            
            if s < n:
                low = mid + 1
            
            elif s > n:
                high = mid - 1
            
            else:
                return mid
        
        return high
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m * k: return -1
        
        def check(min_day):
            
            adj_flowers, bouquets = 0, 0
            
            for day in bloomDay:
                
                adj_flowers = (adj_flowers + 1) if day <= min_day else 0
                
                if adj_flowers == k:
                    bouquets += 1
                    if bouquets == m:
                        return True
                    adj_flowers = 0
                    
            return False
            
            
        
        low = 0
        high = max(bloomDay)
        h = high + 1
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low
        
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        
        def check(x):
            tm = m - 1
            cur = position[0]
            
            for i in range(1, len(position)):
                if position[i] - cur >= x:
                    cur = position[i]
                    tm -= 1
                if tm == 0:
                    return True
            return tm <= 0
        
        
        low = 1
        high = position[-1] - position[0]
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
            
        
        return high
        
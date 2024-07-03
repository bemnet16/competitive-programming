class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        
        def check(x):
            removed = set(removable[:x])
            p_idx = 0
            for i in range(len(s)):
                if i in removed:
                    continue
                    
                if s[i] == p[p_idx]:
                    p_idx += 1
                    
                if p_idx == len(p):
                    return True
            
            return p_idx == len(p)
        
        
        
        
        low = 0
        high = len(removable)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
            
        
        return high
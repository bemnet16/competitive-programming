# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        first_bad = float("inf")
        
        left = 0
        right = n
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                first_bad = min(first_bad, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        
        
        return first_bad
                
            
        
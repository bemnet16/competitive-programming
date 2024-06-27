class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        
        def check(x):
            
            pairs = 0
            i, j = 0, 1
            while i < len(nums) and j < len(nums):
                
                if abs(nums[i] - nums[j]) <= x:
                    i += 2
                    j += 2
                    pairs += 1
                    
                else:
                    i += 1
                    j += 1
                
                if pairs == p:
                    return True
            
            return pairs >= p
                    
        
        
        low, high = 0, 10 ** 9
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        
        return low
        
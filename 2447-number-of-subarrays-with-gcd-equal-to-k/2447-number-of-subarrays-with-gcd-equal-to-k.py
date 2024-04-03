import math

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if nums[j] % k:
                    continue
                    
                if math.gcd(*nums[i:j + 1]) == k:
                    count += 1
                
        
        
        
        return count
                
        
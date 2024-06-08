class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        tot = 0
        reminders = {0:0}
        
        for i, num in enumerate(nums):
            
            tot += num
            
            if (tot % k) == 0 and i >= 1:
                return True
            
            if  (tot % k) in reminders:
                if i - reminders[(tot % k)] >= 2:
                    return True
                
            else:
                reminders[(tot % k)] = i
        
        
        return False
        
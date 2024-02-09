class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        length = len(nums)
        reminder = sum(nums) % p
        
        ## No need to remove anything
        if reminder == 0:
            return 0
        
        # Initialize variables
        prefix_sum = 0
        answer = float("inf")
        tracker = {0: -1}
        
        for i in range(length):
            
            prefix_sum += nums[i]
            temp = (prefix_sum % p - reminder) % p
            if temp in tracker:
                answer = min(answer, i - tracker[temp])
            tracker[prefix_sum % p] = i
        
        return answer if answer < length else -1
                
                
                
                
                
                
                
                
                
                
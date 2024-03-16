class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        count = 0
        maxlen = 0
        track = {0: -1}
        
        for i in range(len(nums)):
            
            count += -1 if nums[i] == 0 else 1
            
            if count in track:
                maxlen = max(maxlen, (i - track[count]))
        
            else:
                track[count] = i
                
                
        return maxlen
            
            
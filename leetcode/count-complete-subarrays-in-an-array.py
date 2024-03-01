class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        s_nums = set(nums)
        distincts = len(s_nums)
        subarrays = 0
        
        for i in range(len(nums)):
            
            temp_set = set()
            for j in range(i, len(nums)):
                temp_set.add(nums[j])
                
                if len(temp_set) == distincts:
                    subarrays += 1
        
        
        return subarrays
        
        
        
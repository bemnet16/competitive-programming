class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        _type = None
        i = 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1
            
        if i >= len(nums):
            return True
            
        if nums[i] > nums[i - 1]:
            _type = 'inc'

        else:
            _type = 'dec'
            
        
        if _type == 'inc':
            for j in range(i, len(nums)):
                if nums[j - 1] > nums[j]:
                    return False
        
        else:
            for j in range(i, len(nums)):
                if nums[j - 1] < nums[j]:
                    return False
        
        return True

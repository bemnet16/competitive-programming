class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                # give the correct position for the numbers that are within the range
                if 0 < nums[i] and nums[i] < n:
                    
                    if nums[i] == nums[temp]:
                        break
                        
                    nums[i], nums[temp] = nums[temp], nums[i]
                    
                else:
                    break
        
        
        for i, num in enumerate(nums):
            
            if i != (num - 1):
                return i + 1
        
        return max(nums) + 1
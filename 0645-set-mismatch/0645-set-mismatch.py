class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        duplicated = None
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    duplicated = nums[i]
                    break
                
                else:
                    nums[i], nums[temp] = nums[temp], nums[i]
                
        
        for i, num in enumerate(nums):
            
            if i != (num - 1):
                return [duplicated, i + 1]
        
        
        
        
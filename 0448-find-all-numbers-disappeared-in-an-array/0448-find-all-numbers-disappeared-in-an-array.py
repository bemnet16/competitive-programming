class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            
            while i != (nums[i] - 1):
                
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    break
                else:
                    nums[i], nums[temp] = nums[temp], nums[i]
        
        
        disappeared = set()
        
        for i, num in enumerate(nums):
            
            if i != (num - 1):
                disappeared.add(i + 1)
        
        
        return disappeared
        
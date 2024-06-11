class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        idx = 0
        
        for i, num in enumerate(nums):
            
            if num % 2 == 0:
                nums[idx], nums[i] = num, nums[idx]
                idx += 1
        
        return nums
        
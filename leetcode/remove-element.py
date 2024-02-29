class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        left_idx = -1
        
        for r in range(len(nums)):
            
            if nums[r] != val:
                
                left_idx += 1
                nums[left_idx], nums[r] = nums[r], nums[left_idx]
        
        return left_idx + 1
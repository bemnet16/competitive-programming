class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left_index = 0
        
        for i in range(1, len(nums)):
            
            if nums[left_index] != nums[i]:
                left_index += 1
                nums[left_index], nums[i] = nums[i], nums[left_index]
        
        return (left_index + 1)
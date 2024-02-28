class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        max_operation = 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            cur_sum = nums[left] + nums[right]
            
            if cur_sum < k:
                left += 1
            
            elif cur_sum > k:
                right -= 1
            
            else:
                max_operation += 1
                
                left += 1
                right -= 1
        
        
        return max_operation
        
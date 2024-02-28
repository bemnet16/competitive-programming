class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        num_pairs = 0
        
        while left < right:
            
            cur_sum = nums[left] + nums[right]
            
            if cur_sum < target:
                num_pairs += (right - left)
                left += 1
            
            else:
                right -= 1
        
        
        return num_pairs
        
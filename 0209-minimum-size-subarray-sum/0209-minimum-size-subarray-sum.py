class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        min_length = len(nums) + 1
        cur_sum = 0
        
        while right < len(nums):
            
            cur_sum += nums[right]
            
            while cur_sum >= target and left <= right:
                
                min_length = min(min_length, (right - left + 1))
                cur_sum -= nums[left]
                left += 1
                

            right += 1
        
        
        return min_length if min_length < len(nums) + 1 else 0
        
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        frequency = defaultdict(int)
        max_subarray = 0
        left = 0
        
        for right in range(len(nums)):
            
            frequency[nums[right]] += 1
            
            while frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
                    
            max_subarray = max(max_subarray, (right - left + 1))
        
        
        return max_subarray
                
        
        
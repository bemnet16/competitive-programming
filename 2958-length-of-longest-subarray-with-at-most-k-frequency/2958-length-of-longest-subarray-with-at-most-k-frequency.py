class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        hashmap = defaultdict(int)
        max_subarray = 0
        left = 0
        
        for right in range(len(nums)):
            
            hashmap[nums[right]] += 1
            
            while hashmap[nums[right]] > k:
                hashmap[nums[left]] -= 1
                left += 1
                    
            max_subarray = max(max_subarray, (right - left + 1))
        
        
        return max_subarray
                
        
        
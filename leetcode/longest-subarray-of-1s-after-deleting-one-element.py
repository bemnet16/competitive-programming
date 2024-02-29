class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeros = 0
        right = 0
        left = 0
        longest = 0
        
        
        while right < len(nums):
            
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                
                zeros -= (nums[left] == 0)
                left += 1
                
                
            
            longest = max(longest, (right - left))
            
            right += 1
        
        
        return longest
            
            
        

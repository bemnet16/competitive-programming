class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start = 0
        num_zeros = 0
        longest_ones = 0
        
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                num_zeros += 1
                
            while num_zeros > k:
                
                num_zeros -= (nums[start] == 0)
                
                start += 1
            
            
            longest_ones = max(longest_ones, (i - start + 1))
        
        
        return longest_ones
        
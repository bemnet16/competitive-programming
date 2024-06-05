class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 in num_set:
                continue
            
            cur = num
            count = 0
            
            while cur in num_set:
                count += 1
                cur += 1
            
            longest = max(longest, count)
        
        
        return longest

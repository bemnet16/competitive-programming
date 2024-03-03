class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        frequency = defaultdict(int)
        frequency[0] = 1
        num_nice = 0
        odd_prefix = 0
        
        for i in range(len(nums)):
            
            if nums[i] & 1:
                odd_prefix += 1
            
            if odd_prefix - k in frequency:
                num_nice += frequency[odd_prefix - k]
            
            frequency[odd_prefix] += 1
        
        
        return num_nice
            
            
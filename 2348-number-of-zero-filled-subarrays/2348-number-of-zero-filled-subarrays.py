class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zero_sequences = 0
        subarrays = 0
        
        for num in nums:
            if num == 0:
                zero_sequences += 1
                subarrays += zero_sequences
            else:
                zero_sequences = 0
        
        return subarrays
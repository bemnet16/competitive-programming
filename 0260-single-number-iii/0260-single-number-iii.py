class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        all_xor = 0
        
        for num in nums:
            all_xor ^= num
        
        
        i = 0
        while not(all_xor & (1 << i)):
            i += 1
        
        
        temp = 0
        
        for num in nums:
            if num & (1 << i):
                temp ^= num
                
        
        return [temp, temp ^ all_xor]
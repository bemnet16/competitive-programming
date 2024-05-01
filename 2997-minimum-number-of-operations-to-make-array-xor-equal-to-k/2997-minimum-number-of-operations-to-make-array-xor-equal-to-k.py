class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        all_xor = 0
        for num in nums:
            all_xor ^= num
        
        
        return bin(all_xor ^ k).count('1')
        
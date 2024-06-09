class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        mod_counts = defaultdict(int)
        mod_counts[0] = 1
        prefixMod = 0
        subarrays = 0
        
        for num in nums:
            
            prefixMod = (prefixMod + num) % k
            subarrays += mod_counts[prefixMod]
            mod_counts[prefixMod] += 1
        
        
        return subarrays
            
        
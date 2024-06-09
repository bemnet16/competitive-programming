class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        mod_counts = defaultdict(int)
        mod_counts[0] = 1
        tot = 0
        subarrays = 0
        
        for num in nums:
            
            tot += num
            subarrays += mod_counts[(tot % k)]
            mod_counts[(tot % k)] += 1
        
        
        return subarrays
            
        
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        min_ope = 0
        
        for num, freq in counter.items():
            
            if freq < 2:
                return -1
            
            if (freq % 3) == 0:
                min_ope += freq // 3
            
            else:
                while freq % 3 != 0:
                    min_ope += 1
                    freq -= 2
                min_ope += freq // 3
                    
                
        return min_ope
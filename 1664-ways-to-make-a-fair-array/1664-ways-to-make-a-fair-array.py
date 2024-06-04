class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        odd_fix = []
        even_fix = []
        
        odd_sum = 0
        even_sum = 0
        
        for i, num in enumerate(nums):
            
            if i % 2 == 0:
                even_sum += num
            
            else:
                odd_sum += num
            
            odd_fix.append(odd_sum)
            even_fix.append(even_sum)
        
        
        indices = 0
        for i, num in enumerate(nums):
            
            if i % 2 == 0:
                pre_odd = odd_fix[i]
                pre_even = even_fix[i] - num
            
            else:
                pre_odd = odd_fix[i] - num
                pre_even = even_fix[i]
                
            suf_odd = even_sum - even_fix[i]
            suf_even = odd_sum - odd_fix[i]
                
            if pre_odd + suf_odd == pre_even + suf_even:
                indices += 1
        
        
        return indices
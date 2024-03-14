class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(x):
            
            split_count = 1
            cur_sum = 0
            
            for num in nums:
                
                cur_sum += num
                
                if cur_sum > x:
                    cur_sum = num
                    split_count += 1
                
                
            return split_count <= k
        
        
        low = max(nums)
        high = sum(nums)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if check(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return low
        
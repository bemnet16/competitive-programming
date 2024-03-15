class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        sum_close = float("inf")
        
        
        for i, val in enumerate(nums):
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                
                three_sum = val + nums[l] + nums[r]
                
                if abs(target - three_sum) < abs(target - sum_close):
                    sum_close = three_sum
                
                if three_sum == target:
                    return target
                
                elif three_sum > target:
                    r -= 1
                
                else:
                    l += 1
                    
        
        return sum_close
        
        
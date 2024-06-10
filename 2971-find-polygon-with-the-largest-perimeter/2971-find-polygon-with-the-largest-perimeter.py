from itertools import accumulate

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        prefix_sum = 0
        perimeter = -1
        
        for i in range(len(nums)):
            if prefix_sum > nums[i]:
                perimeter = prefix_sum + nums[i]
            prefix_sum += nums[i]
                
        
        return perimeter
        
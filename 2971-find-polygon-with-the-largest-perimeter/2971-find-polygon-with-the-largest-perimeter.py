from itertools import accumulate

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        prefix_sum = list(accumulate(nums))
        
        for i in range(len(nums) - 1, 1, -1):
            if prefix_sum[i - 1] > nums[i]:
                return prefix_sum[i]

        
        return -1
        
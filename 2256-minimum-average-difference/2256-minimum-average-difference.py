from math import floor

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        
        _min = float("inf")
        
        for i, num in enumerate(nums):
            
            pre_ava = floor(num / (i + 1))
            if (len(nums) - i - 1) == 0:
                nex_ava = 0
            else:
                nex_ava = floor((nums[-1] - num) / (len(nums) - i - 1))
            
            nums[i] = abs(pre_ava - nex_ava)
            _min = min(_min, nums[i])
        
        return nums.index(_min)
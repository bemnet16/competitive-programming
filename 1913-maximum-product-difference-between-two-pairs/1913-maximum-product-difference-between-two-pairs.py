class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        return (nums[-2] * nums[-1]) - (nums[0] * nums[1])
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums) - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        
        nums.pop()
        
        return self.triangularSum(nums)
        
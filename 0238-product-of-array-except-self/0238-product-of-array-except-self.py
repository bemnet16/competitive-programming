class Solution(object):
    def productExceptSelf(self, nums):
        f_sum = [1] * (len(nums) + 1)
        b_sum = [1] * (len(nums) + 1)
        
        for i in range(1,len(nums) + 1):
            f_sum[i] = f_sum[i - 1] * nums[i - 1]
            b_sum[-i - 1] = b_sum[-i] * nums[-i] 
        
        for i in range(len(nums)):
            nums[i] = f_sum[i] * b_sum[i + 1]
        
        return nums
        
        
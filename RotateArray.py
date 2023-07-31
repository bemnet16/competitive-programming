class Solution(object):
    def rotate(self, nums, k):
        # k=k%len(nums)
        # for i,v in enumerate(nums[len(nums)-k:]+nums[:len(nums)-k]):
        #     nums[i]=v
        # return nums
        
        k=k%len(nums)
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        

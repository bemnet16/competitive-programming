class Solution(object):
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if i==j:continue
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        # for i,val in enumerate(nums):
        #     if (target-val) in nums[i+1:]:
        #         return [i,nums[i+1:].index(target-val)+len(nums[:i+1])]
        
        d={}
        for i,v in enumerate(nums):
            if target-v in d:
                return [d[target-v],i]
            d[v]=i
            
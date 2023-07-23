class Solution(object):
    def arrayChange(self, nums, operations):
        
        d={}
        for i,v in enumerate(nums):
            d[v]=i
        for i,j in operations:
            d[j]=d[i]
            nums[d[i]]=j
        return nums

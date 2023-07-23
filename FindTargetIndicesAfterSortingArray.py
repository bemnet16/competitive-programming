class Solution(object):
    def targetIndices(self, nums, target):
        
        res=[]
        lg=len(nums)
        for i in range(lg):
            for j in range((i+1),lg):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
            if nums[i]==target:
                res.append(i)
            elif nums[i]>target:
                return res
        return res
                

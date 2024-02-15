class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            d = dict()
            for j in range(i+1, len(nums)):
                if -nums[i] - nums[j] in d:
                    res.add((nums[i],-nums[i] - nums[j],nums[j]))
                else:
                    d[nums[j]] = j
        
        return res
class Solution(object):
    def findMiddleIndex(self, nums):
        p_sum = [nums[0]]
        for i in range(1,len(nums)):
            p_sum.append(p_sum[i - 1] + nums[i])
            
        tot = p_sum[-1]
        for idx in range(len(nums)):
            if tot - p_sum[idx] == p_sum[idx] - nums[idx]:
                return idx
        
        return -1
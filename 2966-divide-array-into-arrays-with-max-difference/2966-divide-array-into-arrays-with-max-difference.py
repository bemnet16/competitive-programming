class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        
        for i in range(len(nums)/3):
            st = i * 3
            en = (i * 3) + 3
            if nums[en - 1] - nums[st] > k:
                return []
            temp = nums[st:en]
            res.append(temp)
        
        return res
class Solution(object):
    def majorityElement(self, nums):
        v=[]
        for i in nums:
            if i in v:continue
            if nums.count(i)>(len(nums)/2):return i
            v.append(i)

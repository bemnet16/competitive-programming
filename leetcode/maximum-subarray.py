class Solution(object):
    def maxSubArray(self, nums):
        rm=-10001
        cm=0
        for i in nums:
            cm=max(i,cm+i)
            rm=max(rm,cm)
        return rm
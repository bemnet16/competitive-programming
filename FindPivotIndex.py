class Solution(object):
    def pivotIndex(self, nums):
        tot=sum(nums)
        su=0
        for i in range(len(nums)):
            if su==tot-su-nums[i]:
                return i
            su+=nums[i]
        return -1
